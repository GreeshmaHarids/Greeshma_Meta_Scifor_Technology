import streamlit as st
# from file_1_copy import *
# import datetime
from speech_recognition import Recognizer, AudioFile
from gtts import gTTS
import wikipedia
import webbrowser
import pyjokes
import time
import io
import nltk 
from nltk import word_tokenize, pos_tag
import datetime

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

st.set_page_config('Voice Bot by Greeshma Haridas',
                    "🤖",
                    initial_sidebar_state="expanded",
                    layout="centered")

# UI


title_alignment = """
    <style>
    .centered-title {
        text-align: center;
        color: White;
        font-family: "Lucida Console";
        white-space: nowrap;
    }
    </style>
    <h1 class="centered-title"><b>VOICE BOT</b></h1>
"""

st.markdown("""
    <style>
    .centered-text {
        text-align: center;
        color: White;
        font-family: "Lucida Console";
        white-space: nowrap;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col2:
    st.image("Major_Project/bot_image.png", use_container_width=True)
    st.caption("<p class='centered-text' style='color: #808080;'><b>Let's Chat! I'm Here to Help.</b></p>", unsafe_allow_html=True)
    st.markdown(title_alignment, unsafe_allow_html=True)
    

recognizer = Recognizer()

# Text-to-speech function
def text_speech(text):
    tts = gTTS(text=text, lang='en')
    speech_bytes = io.BytesIO()
    tts.write_to_fp(speech_bytes)
    speech_bytes.seek(0)
    return speech_bytes

# Capture audio and transcribe
def takeCommand(audio_file):
    if audio_file:
        st.write("Audio file detected.")
        audio_bytes = audio_file.getvalue()
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_bytes)
        with AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-in')
            return text
             
        except Exception as e:
            st.write("Error during transcription: ", st.error(e))
            return ""
    
    else:
        st.write("No audio input detected.")
        return ""

# Initialize session state
if "audio_file" not in st.session_state:
    st.session_state.audio_file = None
if "transcribed_text" not in st.session_state:
    st.session_state.transcribed_text = ""
if "response_audio" not in st.session_state:
    st.session_state.response_audio = None

# Step 1: Capture audio input from user
audio_file = st.audio_input("Say something")
if audio_file:
    st.session_state.audio_file = audio_file

# Step 2: Run bot when button is clicked
if st.button("Run Bot",help='Click to start voice bot',use_container_width=True):
    if st.session_state.audio_file:
        st.session_state.transcribed_text = takeCommand(st.session_state.audio_file)
    else:
        st.write("Please record audio first.")

# Step 3: Process and respond to transcription

try:
    if st.session_state.transcribed_text:
        transcribed_text = st.session_state.transcribed_text.lower()
        st.write(f"User said: {transcribed_text}")

        # Simple conversational logic
        if any(word in transcribed_text for word in ['hi', 'hello', 'hey']):
            response_text = "Hi! How can I help you today?"
        

                

        elif any(word in transcribed_text for word in ['who', 'what', 'where', 'wikipedia', 'search']):
            try:
                query_tokens = word_tokenize(transcribed_text)
                essential_words = [word for word, tag in pos_tag(query_tokens) if tag in ['NN', 'NNP']]
                query = " ".join(essential_words)
                with st.spinner(f"Searching for.....{query}"):
                    st.write(f"Searched for {query}")
                    search_results = wikipedia.search(query)
                    if search_results:
                        best_match = search_results[0]
                        response_text = wikipedia.summary(best_match, sentences=1)
                        

                        estimated_duration = int(len(response_text.split()))
                            # Display spinner while "reading"
                                                    
                    else:
                            st.write("I couldn't find anything on Wikipedia.")
            except Exception as e:
                st.error("Oops! Your query is too broad. Please refine your search.")
                st.write("Here are some suggestions:")

                        # Display options for the user
                for option in e.options:
                    if st.button(option):  # Create a button for each option
                        try:
                            response_text = wikipedia.summary(option,sentences=1)
                            st.write(f"**{option}:** {response_text}")
                        except Exception as ex:
                            st.error(f"Error retrieving summary for {option}: {ex}")
                

        
        elif "open youtube" in transcribed_text:
            webbrowser.open("youtube.com")
            st.write("Opened Youtube in Browser")
            time.sleep(3)

        elif "open google" in transcribed_text:
            webbrowser.open("https://www.google.com")
            st.write("Opened Google in Browser")
            time.sleep(3)

        elif 'time' in transcribed_text or 'date' in transcribed_text:
                    now = datetime.datetime.now()

                    # Format date and time
                    formatted_date = now.strftime("%B %d, %Y")
                    formatted_time = now.strftime("%I:%M %p").lower()

                    # Final reply
                    st.write(f"Today is {formatted_date}, and the time is {formatted_time}.")
                    response_text=f"Today is {formatted_date}, and the time is {formatted_time}."

        elif 'joke' in transcribed_text:
                    jokes = pyjokes.get_joke()
                    response_text=f"Here it comes!{jokes}"
                    st.write(f"**Joke:**\n\n```{jokes}```")
                    time.sleep(3)

        elif any(word in transcribed_text for word in ['thank you', 'thanks']):
                    response_text="You're welcome!"
                    st.write("You're welcome!")

        elif any(word in transcribed_text for word in ['exit', 'bye', 'goodbye', 'end']):
            response_text = "Thanks for giving me your time!"
            st.write("Thanks for giving me your time 😊!")

        elif transcribed_text==transcribed_text.lower():
            try:
                query_tokens = word_tokenize(transcribed_text)
                essential_words = [word for word, tag in pos_tag(query_tokens) if tag in ['NN', 'NNP']]
                query = " ".join(essential_words)
                with st.spinner(f"Searching for.....{query}"):
                    st.write(f"Searched for {query}")
                    search_results = wikipedia.search(query)
                    if search_results:
                        best_match = search_results[0]
                        response_text = wikipedia.summary(best_match, sentences=1)
                        

                        estimated_duration = int(len(response_text.split()))
                            # Display spinner while "reading"
                                                    
                    else:
                            st.write("I couldn't find anything on Wikipedia.")
            except Exception as e:
                st.error("Oops! Your query is too broad. Please refine your search.")
                st.write("Here are some suggestions:")

                        # Display options for the user
                for option in e.options:
                    if st.button(option):  # Create a button for each option
                        try:
                            response_text = wikipedia.summary(option,sentences=1)
                            
                        except Exception as ex:
                            st.error(f"Error retrieving summary for {option}: {ex}")
                
             

        else:
            response_text = "Sorry, I didn't understand that."

        # Convert response to speech
        st.session_state.response_audio = text_speech(response_text)
        
        # Output the bot's response as audio and text
        st.write(f"Bot says: {response_text}")
        st.audio(st.session_state.response_audio, format="audio/wav", start_time=0)
        
except Exception as e:
     st.write(e)
     st.write("Please try one more time")
       

if st.button("Exit", use_container_width=True):
    st.audio(text_speech("Thanks for giving me your time"), format="audio/wav", start_time=0)
    st.markdown('<p class="centered-text"><b>Thanks for giving me your time 😊!</b></p>', unsafe_allow_html=True)
    st.stop()


st.sidebar.header("User Guidance",divider="violet")

st.sidebar.markdown("""
1. **Start Chatting**: Click the "Ask" button to begin interacting with the voice bot.
2. **Voice Commands**: You can ask the bot questions like:
   - "What is the time / date?"
   - "Search for [topic] on Wikipedia using keywords like [topic],[what],[where][who],[search][wikipedia]"
   - "Tell me a joke"
   - "Open Google or YouTube"
   - And much more!

3. **Exit**: When you're done, simply click the "Exit" button to end the session.

4. **Greeting**: The bot will greet you based on the time of day and ask how it can assist you.

**Note**: The bot listens to your commands and responds with either a voice output or a text message.

Enjoy your time with the Voice Bot! 😊
""")




st.sidebar.markdown("""
<div style=
        "font-size: 10px; 
        text-align:right;
        bottom:0;
        color:#C1AFD2;
        width: auto;
        background-color:#4A168E;">
        <b>Created By Greeshma Haridas</b>
</div>
""", unsafe_allow_html=True)