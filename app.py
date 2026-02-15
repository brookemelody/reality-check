import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os

# --- 1. UI CONFIGURATION ---
st.set_page_config(page_title="The Agency", page_icon="🕵️‍♂️", layout="centered")
st.title("🕵️‍♂️ The Agency: AI Media Interrogator")
st.markdown("---")

# --- 2. THE BRAIN (MODEL ARCHITECTURE) ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@st.cache_resource # Keeps the model in memory to prevent reload lag
def load_trained_model(checkpoint_path):
    if not os.path.exists(checkpoint_path):
        return None
        
    # Replicate the exact architecture from your training script
    model = models.resnet50()
    model.fc = nn.Sequential(
        nn.Linear(2048, 512),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(512, 1),
        nn.Sigmoid()
    )
    
    try:
        model.load_state_dict(torch.load(checkpoint_path, map_location=device))
        model.to(device)
        model.eval()
        return model
    except Exception as e:
        st.error(f"Error loading brain: {e}")
        return None

# --- 3. FORENSIC TRANSFORMS ---
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# --- 4. THE INTERROGATION INTERFACE ---
st.sidebar.header("Agent Status")
gpu_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU"
st.sidebar.write(f"Hardware: **{gpu_name}**")

# Load model once at startup
model = load_trained_model('agency_brain_e3.pth')

if model is None:
    st.error("🚨 Agency Brain ('agency_brain_e3.pth') not found in folder. Please ensure training is complete.")
else:
    st.sidebar.success("Brain Module: Online")

uploaded_file = st.file_uploader("Upload suspect media for deep-pixel analysis...", type=["jpg", "png", "jpeg"])

if uploaded_file and model is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption="Suspect Image", width='stretch')    
    if st.button("Commence Interrogation"):
        with st.spinner("Analyzing artifacts..."):
            # Prepare image for the 4060
            img_t = preprocess(img).unsqueeze(0).to(device)
            
            # Predict
            with torch.no_grad():
                prediction = model(img_t).item()
            
            # Results Display
            st.markdown("### Forensic Findings")
            if prediction > 0.5:
                st.error("🚨 **RESULT: AI GENERATED**")
                confidence = prediction
            else:
                st.success("✅ **RESULT: REAL MEDIA**")
                confidence = 1 - prediction

            st.metric("Confidence Score", f"{confidence:.2%}")
            
            if confidence > 0.90:
                st.warning("High-probability digital manipulation detected.")