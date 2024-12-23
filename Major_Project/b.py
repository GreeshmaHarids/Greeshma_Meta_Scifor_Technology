import streamlit as st
from gtts import gTTS
import tempfile
import base64

# Function to convert text to speech and play aloud
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    # Create a temporary file to save the speech
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        file_path = tmpfile.name
        tts.save(file_path)  # Save the audio to the temp file
    return file_path

# Function to autoplay the audio
def autoplay_audio(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        b64_audio = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mpeg">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Streamlit UI for text input
st.title("Text to Speech - Auto Play")

# Text input from the user
user_input = st.text_area("Enter text to convert to speech:")

if user_input:
    # Convert text to speech and play aloud
    autoplay_audio(convert_text_to_speech(user_input))
