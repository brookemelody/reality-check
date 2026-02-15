import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torchvision import models

# --- 1. SETUP ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = 'agency_brain_e5.pth' 

test_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Loading 20,000 test images with forced indices
test_data = datasets.ImageFolder('data/test', transform=test_transforms)
test_data.class_to_idx = {'REAL': 0, 'FAKE': 1} 
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

# --- 2. LOAD MODEL ---
model = models.resnet50()
model.fc = nn.Sequential(
    nn.Linear(2048, 512), nn.ReLU(), nn.Dropout(0.3),
    nn.Linear(512, 1), nn.Sigmoid()
)
model.load_state_dict(torch.load(MODEL_PATH))
model.to(device)
model.eval()

# --- 3. FORENSIC EVALUATION ---
true_positives = 0  # Correctly caught fakes
false_positives = 0 # Real images wrongly called fake
true_negatives = 0  # Correctly identified real images
false_negatives = 0 # Fakes that slipped through

print("🕵️‍♂️ Commencing Forensic Evaluation of 20,000 images...")

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device).float().view(-1, 1)
        outputs = model(images)
        predictions = (outputs > 0.5).float()
        
        for p, l in zip(predictions, labels):
            if p == 1 and l == 1: true_positives += 1
            elif p == 1 and l == 0: false_positives += 1
            elif p == 0 and l == 0: true_negatives += 1
            elif p == 0 and l == 1: false_negatives += 1

# --- 4. THE SCOREBOARD ---
total = len(test_data)
accuracy = (true_positives + true_negatives) / total
fpr = false_positives / (false_positives + true_negatives) # Rate of false accusations

print(f"\n--- Agency Forensic Report ---")
print(f"Overall Accuracy: {accuracy:.2%}")
print(f"False Positive Rate: {fpr:.2%}") # Crucial metric for judges
print(f"Fakes Captured: {true_positives} / 10,000")
print(f"Real Images Verified: {true_negatives} / 10,000")