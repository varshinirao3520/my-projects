# Import necessary libraries
import streamlit as st
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler
import torch
import base64
import time
from PIL import Image

@st.cache_resource(show_spinner=False)
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    
    # Set a robust scheduler (LMSDiscreteScheduler)
    scheduler = LMSDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    
    # Load the Stable Diffusion pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        scheduler=scheduler,
        torch_dtype=torch.float32  # Ensure compatibility with CPU
    ).to("cpu")
    return pipe

pipe = load_model()

def get_image_download_link(img_path, filename):
    with open(img_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    return f'<a href="data:file/png;base64,{b64}" download="{filename}">📥 Download Image</a>'

st.set_page_config(page_title="AI Image Generator 🎨", layout="wide")
st.title("🖼️ AI Image Generator 🎨")
st.write("Generate stunning AI-powered realistic images using AI!")

st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stTextInput, .stButton {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

prompt = st.text_input("📝 Enter a prompt:", "A futuristic cyberpunk city with neon lights")

if st.button("🎨 Generate Image"):
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 101, 20):
        time.sleep(1)
        progress_bar.progress(i)
        status_text.text(f"Processing... {i}% done")

    with st.spinner("AI is generating your image... ⏳"):
        image = pipe(prompt, height=512, width=512).images[0]
    
    st.image(image, caption="🖼️ Generated Image", use_column_width=True)
    image.save("generated_image.png")
    st.success("✅ Image Generated Successfully!")

    st.markdown(get_image_download_link("generated_image.png", "AI_Art.png"), unsafe_allow_html=True)
    progress_bar.empty()
    status_text.empty()