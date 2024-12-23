import streamlit as st
from gtts import gTTS
import base64
import io
import time

# Function to convert text to speech and return in-memory audio
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Function to autoplay the audio
def autoplay_audio(audio_buffer):
    b64_audio = base64.b64encode(audio_buffer.read()).decode()
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mpeg">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Streamlit UI for text input
st.title("Text to Speech - In-Memory Playback")

# Text input from the user
user_input = st.text_area("Enter text to convert to speech:")

if user_input:
    # Convert text to speech and play aloud    
    # Estimate duration (approx. 2.5 words/sec)
    estimated_duration = len(user_input.split()) / 2.5

    # Display spinner while "reading"
    with st.spinner("Reading text aloud, please wait..."):
        autoplay_audio(convert_text_to_speech(user_input))
        time.sleep(estimated_duration)  # Simulate waiting for audio playback to complete
    st.success("Finished reading!")
