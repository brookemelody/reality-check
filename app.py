import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

st.set_page_config(page_title="The Agency", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ The Agency: AI Media Interrogator")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
st.sidebar.write(f"Connected to: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")

uploaded_file = st.file_uploader("Upload suspect media...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption="Suspect Image", use_container_width=True)
    st.info("Pixels under interrogation... (Waiting for trained model)")