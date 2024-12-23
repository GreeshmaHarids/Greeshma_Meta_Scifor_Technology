import streamlit as st
from gtts import gTTS
import tempfile

# Function to convert text to speech
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    # Create a temporary file to save the speech
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        file_path = tmpfile.name
        tts.save(file_path)  # Save the audio to the temp file
    return file_path

# Streamlit UI for text input and file upload
st.title("Text to Speech Converter")

# Text input from the user
user_input = st.text_area("Enter text to convert to speech:")

if user_input:
    # Convert text to speech and get the file path
    audio_file_path = convert_text_to_speech(user_input)
    
    # Display the audio player
    st.audio(audio_file_path, format='audio/mp3')

# Optionally, allow users to upload their own text file
uploaded_file = st.file_uploader("Upload a Text File", type=["txt"])

if uploaded_file is not None:
    # Read the file content
    file_content = uploaded_file.read().decode("utf-8")
    
    # Convert the content to speech and get the file path
    audio_file_path = convert_text_to_speech(file_content)
    
    # Display the audio player
    st.audio(audio_file_path, format='audio/mp3')
