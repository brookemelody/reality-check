import torch
import torch.nn as nn
from torchvision import models, datasets, transforms
from torch.utils.data import DataLoader
from tqdm import tqdm
import os

# 1. CONFIGURATION
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BATCH_SIZE = 32
NUM_WORKERS = 0  # Set to 0 for Windows stability during testing

# 2. DATA TRANSFORMS
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def train():
    print(f"Agent Online: {torch.cuda.get_device_name(0)}")
    
    # 3. LOAD DATASET
    train_path = 'data/train'
    train_dataset = datasets.ImageFolder(train_path, transform=transform)
    
    # DIAGNOSTIC CHECKS
    print(f"Checking data in: {os.path.abspath(train_path)}")
    print(f"Classes found: {train_dataset.classes}")
    print(f"Total images found: {len(train_dataset)}")
    
    if len(train_dataset) == 0:
        print("CRITICAL ERROR: No images found. Check your folder structure!")
        return

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, 
                              num_workers=NUM_WORKERS, pin_memory=True)

    # 4. MODEL ARCHITECTURE (ResNet50)
    model = models.resnet50(weights='IMAGENET1K_V1')
    for param in model.parameters():
        param.requires_grad = False
    # Unfreeze Layer 4 for AI detection fine-tuning
    for param in model.layer4.parameters():
        param.requires_grad = True

    model.fc = nn.Sequential(
        nn.Linear(2048, 512),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(512, 1),
        nn.Sigmoid()
    )
    model = model.to(device)

    # 5. OPTIMIZER & LOSS
    optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.0001)
    criterion = nn.BCELoss()

    # 6. TRAINING LOOP
    print("Initiating Interrogation...")
    model.train()
    for epoch in range(5):
        loop = tqdm(train_loader, desc=f"Epoch {epoch+1}/5")
        for images, labels in loop:
            images, labels = images.to(device), labels.float().to(device).unsqueeze(1)
            
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            loop.set_postfix(loss=loss.item())
        
        torch.save(model.state_dict(), f'agency_brain_e{epoch+1}.pth')

if __name__ == "__main__":
    train()