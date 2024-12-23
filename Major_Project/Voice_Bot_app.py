import streamlit as st
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import pyjokes
import time
import nltk
from gtts import gTTS
import tempfile
import pygame
from nltk import word_tokenize, pos_tag




nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


# creating functions 

def speak(audio):
    # Initialize the gTTS instance
    tts = gTTS(text=audio, lang='en', slow=False)
    
    # Create a temporary file and save the speech as an mp3
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        file_path = tmpfile.name
        tts.save(file_path)  # Save the mp3 to the temporary file path
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the generated mp3 file
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Wait until the audio finishes playing before continuing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
def say_greetings():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak("Good morning!")
        st.write("Good morning.....!")
    elif 12 <= hour < 17:
        speak("Good afternoon!")
        st.write("Good afternoon!")
    elif 17 <= hour < 22:
        speak("Good evening!")
        st.write("Good evening!")
    else:
        speak("Hello ! ")
        st.write("Hello...!")
    speak("How can I help you?")
    st.write("How can I help you?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        st.write("Recognizing............")
        st.spinner("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice")
        return None

    return query

def run_bot():
    clear = lambda: os.system('cls')

    # this fn. will clean any command before execution of this python file
    clear()
    say_greetings()
    

    while True:
        try:
            query = takeCommand()

            if query is None:  # Check if the query is None
                speak("Sorry, I couldn't hear anything. Please try again.")
                st.write("Sorry, I couldn't hear anything. Please try again.")
                st.stop()  # Exit the function and try again

            query = query.lower()  # Convert the query to lowercase
            
            # All the commands said by user will be 
            # stored here in 'query' and will be
            # converted to lower case for easily 
            # recognition of command
            st.write(f"User asked: {query}")
            time.sleep(3)

            if any(word in query for word in ['who', 'what', 'where', 'wikipedia', 'search']):
                try:
                    query_tokens = word_tokenize(query)
                    essential_words = [word for word, tag in pos_tag(query_tokens) if tag in ['NN', 'NNP']]
                    query = " ".join(essential_words)
                    st.write("Searching for.....", query)
                    search_results = wikipedia.search(query)
                    if search_results:
                        best_match = search_results[0]
                        results = wikipedia.summary(best_match, sentences=1)
                        speak(results)
                        st.write(results)
                    else:
                        speak("I couldn't find anything on Wikipedia.")
                        st.write("I couldn't find anything on Wikipedia.")
                except Exception as e:
                    st.error("Oops! Your query is too broad. Please refine your search.")
                    speak("Oops! Your query is too broad. Please refine your search.")
                    st.write("Here are some suggestions:")

                    # Display options for the user
                    for option in e.options:
                        if st.button(option):  # Create a button for each option
                            try:
                                refined_summary = wikipedia.summary(option)
                                st.write(f"**{option}:** {refined_summary}")
                            except Exception as ex:
                                st.error(f"Error retrieving summary for {option}: {ex}")
                    time.sleep(5)


            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")
                st.write("Opened Youtube in Browser")
                time.sleep(3)

            elif 'open google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("https://www.google.com")
                st.write("Opened Google in Browser")
                time.sleep(3)

            elif 'time' in query or 'date' in query:
                now = datetime.datetime.now()

                # Format date and time
                formatted_date = now.strftime("%B %d, %Y")
                formatted_time = now.strftime("%I:%M %p").lower()

                # Final reply
                st.write(f"Today is {formatted_date}, and the time is {formatted_time}.")
                speak(f"Today is {formatted_date}, and the time is {formatted_time}.")

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                st.markdown('<p class="centered-text"><b>Thanks for giving me your time 😊!</b></p>', unsafe_allow_html=True)
                st.stop()

            elif 'joke' in query:
                jokes = pyjokes.get_joke()
                speak(f"Here it comes!{jokes}")
                st.write(f"**Joke:**\n\n```{jokes}```")
                time.sleep(3)

            elif any(word in query for word in ['Thankyou', 'Thanks']):
                speak("You're welcome!")
                st.write("You're welcome!")

            elif any(word in query for word in ['Hi', 'hello','hey','Greetings!']):
                speak("Hey! How can I assist you today? ")
                st.write("Hey! How can I assist you today?")

            elif query == query.lower():
                try:
                    st.write("Searching for.....", query)
                    speak(wikipedia.summary(query, sentences=2))
                    st.write(wikipedia.summary(query, sentences=2))
                    time.sleep(3)
                except Exception as e:
                    st.error("Oops! Your query is too broad. Please refine your search.")
                    speak("Oops! Your query is too broad. Please refine your search.")
                    st.write("Here are some suggestions:")

                    # Display options for the user
                    for option in e.options:
                        if st.button(option):  # Create a button for each option
                            try:
                                refined_summary = wikipedia.summary(option)
                                st.write(f"{option}:{refined_summary}")
                                if refined_summary == None:
                                    st.write("No suggestions")
                            except Exception as ex:
                                st.error(f"Error retrieving summary for {option}: {ex}")

                    time.sleep(5)
            else:
                speak("Sorry couldn't find a result, try one more time")
                st.write("Sorry couldn't find a result, try one more time")


        except AttributeError as a:
            st.write("Unable to recognize your voice")
            speak("Please try one more time, your voice was not recognized")

        except RuntimeError as r:
            st.write("An issue occurred due to multiple clicks. Please restart and try again.")

        # sys.exit(takeCommand())

        time.sleep(2)
        speak("Do you have any other queries? Please ask, I am listening.... ")

        

# UI
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
    if st.button("Ask", use_container_width=True):
        try:
            run_bot()
            st.empty()
        except Exception as e:
            st.write(e)
            st.write("Please try one more time")
            st.stop()

if st.button("Exit", use_container_width=True):
    speak("Thanks for giving me your time")
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