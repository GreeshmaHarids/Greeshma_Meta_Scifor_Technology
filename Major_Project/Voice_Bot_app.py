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
from nltk import word_tokenize, pos_tag
import base64
import io





nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


# creating functions 

def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio_buffer = io.BytesIO()

    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Function to autoplay the audio
def autoplay_audio(audio_buffer):
    # Convert text to speech and play aloud    
    # Estimate duration (approx. 2.5 words/sec)
        
    b64_audio = base64.b64encode(audio_buffer.read()).decode()
    audio_html = f"""
        <audio id="audio-player" autoplay>
            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mpeg">
        </audio>
        <script>
            var audioElement = document.getElementById("audio-player");
            audioElement.onended = function() {{
                // Trigger next action once the current audio finishes
                window.location.reload();
            }};
        </script>
        """
    st.markdown(audio_html, unsafe_allow_html=True)
    time.sleep(2)




def say_greetings():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        autoplay_audio(convert_text_to_speech("Good morning!"))
        st.write("Good morning.....!")
    elif 12 <= hour < 17:
        autoplay_audio(convert_text_to_speech("Good afternoon!"))
        st.write("Good afternoon!")
    elif 17 <= hour < 22:
        autoplay_audio(convert_text_to_speech("Good evening!"))
        st.write("Good evening!")
    else:
        autoplay_audio(convert_text_to_speech("Hello ! "))
        st.write("Hello...!")
    # time.sleep(2)
    autoplay_audio(convert_text_to_speech("How can I help you?"))
    st.write("How can I help you?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        with st.spinner("Listening......."):

            r.pause_threshold = 1
            audio = r.listen(source)

    try:
        with st.spinner("Recognizing"):
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
            time.sleep(2)

            if query is None:  # Check if the query is None
                autoplay_audio(convert_text_to_speech("Sorry, I couldn't hear anything. Please try again."))
                st.write("Sorry, I couldn't hear anything. Please try again.")
                st.stop()  # Exit the function and try again

            query = query.lower()  # Convert the query to lowercase
            
            # All the commands said by user will be 
            # stored here in 'query' and will be
            # converted to lower case for easily 
            # recognition of command
            st.write(f"User asked: {query}")
            

            if any(word in query for word in ['who', 'what', 'where', 'wikipedia', 'search']):
                try:
                    query_tokens = word_tokenize(query)
                    essential_words = [word for word, tag in pos_tag(query_tokens) if tag in ['NN', 'NNP']]
                    query = " ".join(essential_words)
                    with st.spinner(f"Searching for.....{query}"):
                        st.write(f"Searched for {query}")
                    search_results = wikipedia.search(query)
                    if search_results:
                        best_match = search_results[0]
                        results = wikipedia.summary(best_match, sentences=1)
                        autoplay_audio(convert_text_to_speech(results))

                        estimated_duration = int(len(results.split()))
                        st.write(estimated_duration)
                        # Display spinner while "reading"
                        
                        st.write(estimated_duration)
                        time.sleep(10)
                        
                    else:
                        autoplay_audio(convert_text_to_speech("I couldn't find anything on Wikipedia."))
                        st.write("I couldn't find anything on Wikipedia.")
                except Exception as e:
                    st.error("Oops! Your query is too broad. Please refine your search.")
                    autoplay_audio(convert_text_to_speech("Oops! Your query is too broad. Please refine your search."))
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
                autoplay_audio(convert_text_to_speech("Here you go to Youtube\n"))
                webbrowser.open("youtube.com")
                st.write("Opened Youtube in Browser")
                time.sleep(3)

            elif 'open google' in query:
                autoplay_audio(convert_text_to_speech("Here you go to Google\n"))
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
                autoplay_audio(convert_text_to_speech(f"Today is {formatted_date}, and the time is {formatted_time}."))

            elif 'exit' in query:
                autoplay_audio(convert_text_to_speech("Thanks for giving me your time"))
                st.markdown('<p class="centered-text"><b>Thanks for giving me your time 😊!</b></p>', unsafe_allow_html=True)
                st.stop()

            elif 'joke' in query:
                jokes = pyjokes.get_joke()
                autoplay_audio(convert_text_to_speech(f"Here it comes!{jokes}"))
                st.write(f"**Joke:**\n\n```{jokes}```")
                time.sleep(3)

            elif any(word in query for word in ['Thankyou', 'Thanks']):
                autoplay_audio(convert_text_to_speech("You're welcome!"))
                st.write("You're welcome!")

            elif any(word in query for word in ['Hi', 'hello','hey','Greetings!']):
                autoplay_audio(convert_text_to_speech("Hey! How can I assist you today? "))
                st.write("Hey! How can I assist you today?")

            elif query == query.lower():
                try:
                    st.write("Searching for.....", query)
                    results = wikipedia.summary(query, sentences=2)
                    autoplay_audio(convert_text_to_speech(wikipedia.summary(query, sentences=2)))
                    st.write(wikipedia.summary(query, sentences=2))
                    estimated_duration = int(len(results.split())/2)
                    progress = st.progress(0)
                    # for i in range(estimated_duration):
                    #     progress.progress(i + 1)
                    # time.sleep(estimated_duration)
                    for i in range(estimated_duration):
                        progress.progress(int((i + 1) / estimated_duration * 100))  # Update progress bar
                        time.sleep(1)
                    
                    
                        
            
                except Exception as e:
                    st.error("Oops! Your query is too broad. Please refine your search.")
                    autoplay_audio(convert_text_to_speech("Oops! Your query is too broad. Please refine your search."))
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
                autoplay_audio(convert_text_to_speech("Sorry couldn't find a result, try one more time"))
                st.write("Sorry couldn't find a result, try one more time")


        except AttributeError as a:
            st.error(a)
            st.write("Unable to recognize your voice")
            autoplay_audio(convert_text_to_speech("Please try one more time, your voice was not recognized"))

        except RuntimeError as r:
            st.write("An issue occurred due to multiple clicks. Please restart and try again.")

        # sys.exit(takeCommand())

        time.sleep(2)
        autoplay_audio(convert_text_to_speech("Do you have any other queries? Please ask, I am listening.... "))
        time.sleep(2)

        

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
            # st.empty()
        except Exception as e:
            st.write(e)
            st.write("Please try one more time")
            st.stop()

if st.button("Exit", use_container_width=True):
    st.markdown('<p class="centered-text"><b>Thanks for giving me your time 😊!</b></p>', unsafe_allow_html=True)
    autoplay_audio(convert_text_to_speech("Thanks for giving me your time"))
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