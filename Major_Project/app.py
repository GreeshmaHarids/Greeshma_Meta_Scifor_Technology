import streamlit as st
from speech_recognition import Recognizer, AudioFile
from gtts import gTTS
import wikipedia
import pyjokes
import time
import io
import nltk 
from nltk import word_tokenize, pos_tag
import datetime

#ui


st.set_page_config('Voice Bot by Greeshma Haridas',
                    "🤖",
                    initial_sidebar_state="expanded",
                    layout="centered")

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


st.sidebar.info(
    "To use voice features, please allow microphone access when prompted by your browser."
)    

st.sidebar.header("User Guide", divider="violet")

st.sidebar.markdown("""
### **How to Use:**
1. **Start Chatting:**
   - Record your audio using the input provided in the app.
   - Click the **"Run Bot"** button to interact with the bot.

2. **Voice Commands Examples:**
   - **Greet**: Say "Hi", "Hello", or "Hey" to start.
   - **Ask for Time or Date**: Say "What is the time?" or "What is today's date?".
   - **Search Wikipedia**: Use keywords like:
     - "Search for [topic]"
     - "Who is [name]?"
     - "What is [topic]?"
   - **Entertainment**: Say "Tell me a joke."
   - **Open Websites**: Say:
     - "Open Google"
     - "Open YouTube"  
       *(These open the websites in a new browser tab.)*

3. **Exit Chat:**
   - Say "Exit", "Bye", or "Goodbye" to end the session.
   - Alternatively, click the **"Exit"** button.

---

### **Features:**
- **Real-Time Interaction**: The bot listens, processes, and responds to your commands via text and audio.
- **Multifunctionality**:
  - Handles general inquiries.
  - Provides fun responses like jokes.
  - Opens websites or applications directly.
- **Error Handling**: If the bot cannot understand your command, refine your query or use simpler keywords.

---

### **Tips for Best Results:**
- Speak clearly when recording your audio.
- Keep commands concise, e.g., "Tell me about Albert Einstein."
- For Wikipedia searches, use relevant and specific keywords.

---

<div style="
        font-size: 11px; 
        text-align:right;
        bottom:0;
        color:#C1AFD2;
        width: auto;
        background-color:#4A168E;">
        <b>Created By Greeshma Haridas</b>
</div>
""", unsafe_allow_html=True)


#main code

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

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
        st.write("Audio Recorded.")
        audio_bytes = audio_file.getvalue()
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_bytes)
        with AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-in',)
            return text
             
        except Exception as e:
            st.error(f"Error: Unable to transcribe the audio. Please try again")
            return ""
         
    
    else:
        st.write("No audio input detected.")
        return ""


def taketext(text_file):
     if text_file:
          if text_file==None:
               return ""
          else:
               text = text_file
               return text

# Initialize session state
if "audio_file" not in st.session_state:
    st.session_state.audio_file = None
if "transcribed_text" not in st.session_state:
    st.session_state.transcribed_text = ""
if "response_audio" not in st.session_state:
    st.session_state.response_audio = None
if "text_file" not in st.session_state:
     st.session_state.text_file = None




# Step 1: Capture audio input from user
col1,col2=st.columns(2,border=True)
with col1:
    audio_file = st.audio_input("Speak your question or command here!")
    if audio_file:
        st.session_state.audio_file = audio_file
with col2:
    text_file = st.text_input("Or, type your query here!")
    if text_file:
        st.session_state.text_file = text_file
    else:
         st.session_state.text_file = ""

# Step 2: Run bot when button is clicked
if st.button("Run Bot",help='Click to start voice bot',use_container_width=True):

    if st.session_state.text_file:
        st.session_state.transcribed_text = taketext(st.session_state.text_file)

    elif st.session_state.audio_file:
        st.session_state.transcribed_text = takeCommand(st.session_state.audio_file)
    
    
    else:
        st.write("Please record audio or write a query first.")

# Step 3: Process and respond to transcription
try:
    if st.session_state.transcribed_text:
        transcribed_text = st.session_state.transcribed_text.lower()
        st.write(f"User said: {transcribed_text}")

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
                           
                                                    
                    else:
                            st.write("I couldn't find anything on Wikipedia.")
            except Exception as e:
                st.error("Oops! Your query is too broad. Please refine your search.")
                st.write("Here are some suggestions:")

                try:       
                    for option in e.options:
                        if st.button(option):  
                            try:
                                response_text = wikipedia.summary(option,sentences=1)
                                st.write(f"**{option}:** {response_text}")
                            except Exception as ex:
                                st.error(f"Error retrieving summary for {option}: {ex}")
                except Exception as e:
                     st.write("Error searching for options")
                

        
        elif "open youtube" in transcribed_text:

            msg = st.empty()

            msg.warning(
                "To use voice commands like 'Open YouTube', please ensure pop-ups are allowed in your browser."
            )
            time.sleep(3)
            msg.empty()
            st.components.v1.html("""
                <script type="text/javascript">
                    window.open("https://www.youtube.com", "_blank");
                </script>
            """, height=0)
            response_text="Opened Youtube in Browser"

        elif "open google" in transcribed_text:
            msg = st.empty()

            msg.warning(
                "To use voice commands like 'Open Google', please ensure pop-ups are allowed in your browser."
            )
            time.sleep(3)
            msg.empty()
            # webbrowser.open("https://www.google.com")
            st.components.v1.html("""
                <script type="text/javascript">
                    window.open("https://www.google.com", "_blank");
                </script>
            """, height=0) 

            response_text="Opened Google in Browser"

        elif 'time' in transcribed_text or 'date' in transcribed_text:
                    now = datetime.datetime.now()

                    # Format date and time
                    formatted_date = now.strftime("%B %d, %Y")
                    formatted_time = now.strftime("%I:%M %p").lower()

                    # Final reply
                    response_text=f"Today is {formatted_date}, and the time is {formatted_time}."

        elif 'joke' in transcribed_text:
                    jokes = pyjokes.get_joke()
                    response_text=f"Here it comes!{jokes}"

        elif any(word in transcribed_text for word in ['thank you', 'thanks']):
                    response_text="You're welcome!"

        elif any(word in transcribed_text for word in ['exit', 'bye', 'goodbye', 'end']):
            response_text = "Thanks for giving me your time!"
            st.stop()

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
        st.audio(st.session_state.response_audio, format="audio/wav", start_time=0, autoplay=True)

        st.session_state.transcribed_text = ""

    else:
            st.write("No transcribed text to process.")
        
except Exception as e:
     st.error("Please refine your search")
     st.write("Please try one more time")
       

if st.button("Exit", use_container_width=True):
    
    st.markdown('<p class="centered-text" style="color: #808080;"><b>Thanks for giving me your time 😊!</b></p>', unsafe_allow_html=True)
    st.session_state.response_audio = text_speech("Thanks for giving me your time")
    st.audio(st.session_state.response_audio, format="audio/wav", start_time=0,autoplay=True)
    st.stop()

c1,c2,c3=st.columns([4,1,4])
with c2:
    st.button("Clear",help="Click to clear all")