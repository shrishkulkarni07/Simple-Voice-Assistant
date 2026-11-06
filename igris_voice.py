"""
Igris - VOICE ENABLED Version (Educational Project)
====================================================
A voice assistant that LISTENS to your voice and SPEAKS responses!

IMPORTANT: This version does NOT use PyAudio!
Instead, it uses the SpeechRecognition library with Google's Speech API

Created for educational purposes - Easy to understand and explain!
"""

import speech_recognition as sr  # For listening to voice commands
import pyttsx3  # For speaking responses (Text-to-Speech)
import datetime  # For getting current time and date
import webbrowser  # For opening websites
import wikipedia  # For searching Wikipedia
import random  # For random joke selection


# ============================================================================
# SECTION 1: TEXT-TO-SPEECH (Making the computer SPEAK)
# ============================================================================

def get_engine():
    """
    Create a Text-to-Speech (TTS) engine
    
    EXPLANATION FOR YOUR CLASS:
    ---------------------------
    This function creates a "speaking engine" that converts text into speech.
    Think of it like a robot voice that reads text out loud!
    
    How it works:
    1. pyttsx3.init() - Starts the speech engine
    2. We get available voices (male/female options)
    3. We set the speaking speed (150 words per minute)
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Choose first voice (usually male)
    engine.setProperty('rate', 150)  # Speaking speed
    return engine


def speak(text):
    """
    Make the computer speak the given text
    
    EXPLANATION FOR YOUR CLASS:
    ---------------------------
    This is how Igris "talks" to you!
    
    Steps:
    1. Print the text on screen (so you can read it too)
    2. Create a fresh speech engine
    3. Tell the engine to say the text
    4. runAndWait() - Actually speak it out loud!
    """
    print(f"🔊 Igris: {text}")
    try:
        engine = get_engine()
        engine.say(str(text))
        engine.runAndWait()  # This is where the actual speaking happens!
        engine.stop()
    except Exception as e:
        print(f"⚠️ Speech error: {e}")


# ============================================================================
# SECTION 2: SPEECH-TO-TEXT (Making the computer LISTEN)
# ============================================================================

def listen_to_voice():
    """
    Listen to user's voice and convert it to text
    
    *** THIS IS THE MAGIC PART - NO PYAUDIO NEEDED! ***
    
    EXPLANATION FOR YOUR CLASS:
    ---------------------------
    This is how Igris "hears" you!
    
    How Speech Recognition Works:
    1. Microphone captures your voice (sound waves)
    2. Sound is converted to digital audio data
    3. Audio is sent to Google's servers
    4. Google's AI recognizes words in the audio
    5. Text is sent back to our program
    
    Why NO PyAudio?
    ---------------
    - SpeechRecognition library can use different "backends"
    - On Windows, it can use the built-in audio system
    - We use Google's API which doesn't require PyAudio
    
    Technical Flow:
    1. sr.Recognizer() - Creates a "listener" object
    2. sr.Microphone() - Connects to your microphone
    3. recognizer.listen() - Records your voice
    4. recognizer.recognize_google() - Sends audio to Google and gets text back
    """
    recognizer = sr.Recognizer()
    
    # Adjust for ambient noise (important for accuracy!)
    # This "calibrates" the microphone to ignore background noise
    with sr.Microphone() as source:
        print("\n🎤 Adjusting for background noise... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("✅ Ready! Listening for your command...")
        
        try:
            # Listen to the user's voice
            # timeout=5 means wait 5 seconds for user to start speaking
            # phrase_time_limit=10 means maximum 10 seconds of speaking
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            print("🔄 Processing your voice...")
            
            # Send audio to Google and get text back
            # This is where the VOICE becomes TEXT!
            command = recognizer.recognize_google(audio)
            command = command.lower()  # Convert to lowercase for easier matching
            
            print(f"✅ You said: {command}")
            return command
            
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError:
            speak("Sorry, there's a problem with the internet connection.")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None


# ============================================================================
# SECTION 3: ASSISTANT FEATURES (What Igris can do)
# ============================================================================

def greet_user():
    """Greet the user based on time of day"""
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Igris, your voice assistant!")
    speak("You can speak to me, and I'll respond with my voice!")


def tell_time():
    """Tell the current time"""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")


def tell_date():
    """Tell the current date"""
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today is {current_date}")


def tell_joke():
    """Tell a random programming joke"""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar, walks up to two tables and asks: Can I join you?",
        "Why do Java developers wear glasses? Because they cannot see sharp!",
        "How many programmers does it take to change a light bulb? None, that is a hardware problem!",
        "Why did the programmer quit his job? Because he did not get arrays!",
        "What is a programmer's favorite hangout place? Foo Bar!",
        "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25!",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
    ]
    joke = random.choice(jokes)
    speak(joke)


def search_google(query):
    """Search Google for the query"""
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def open_website(site_name):
    """Open popular websites"""
    websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'github': 'https://www.github.com',
        'facebook': 'https://www.facebook.com',
        'twitter': 'https://www.twitter.com',
        'instagram': 'https://www.instagram.com',
        'reddit': 'https://www.reddit.com',
        'stack overflow': 'https://www.stackoverflow.com'
    }
    
    if site_name in websites:
        speak(f"Opening {site_name}")
        webbrowser.open(websites[site_name])
    else:
        speak(f"Sorry, I don't know how to open {site_name}")


def search_wikipedia(query):
    """Search Wikipedia for information"""
    try:
        speak(f"Searching Wikipedia for {query}")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any results on Wikipedia.")
    except:
        speak("Sorry, something went wrong with Wikipedia search.")


# ============================================================================
# SECTION 4: COMMAND PROCESSING (Understanding what user wants)
# ============================================================================

def process_command(command):
    """
    Process the user's voice command and take appropriate action
    
    EXPLANATION FOR YOUR CLASS:
    ---------------------------
    This function is like Igris's "brain"!
    It looks at what you said and decides what to do.
    
    How it works:
    - Uses "if" statements to check for keywords
    - If it finds a match, it calls the appropriate function
    - Returns True to continue, False to exit
    """
    
    # Time command
    if 'time' in command:
        tell_time()
    
    # Date command
    elif 'date' in command or 'today' in command:
        tell_date()
    
    # Joke command
    elif 'joke' in command:
        tell_joke()
    
    # Open website commands
    elif 'open google' in command:
        open_website('google')
    elif 'open youtube' in command:
        open_website('youtube')
    elif 'open github' in command:
        open_website('github')
    
    # Search Google
    elif 'search' in command or 'google' in command:
        search_query = command.replace('search', '').replace('google', '').replace('for', '').strip()
        if search_query:
            search_google(search_query)
        else:
            speak("What should I search for?")
    
    # Wikipedia search
    elif 'wikipedia' in command or 'who is' in command or 'what is' in command:
        search_query = command.replace('wikipedia', '').replace('who is', '').replace('what is', '').strip()
        if search_query:
            search_wikipedia(search_query)
        else:
            speak("What should I search on Wikipedia?")
    
    # Help command
    elif 'help' in command or 'commands' in command:
        show_help()
    
    # Exit commands
    elif 'exit' in command or 'quit' in command or 'bye' in command or 'goodbye' in command:
        speak("Goodbye! Have a great day!")
        return False
    
    # Unknown command
    else:
        speak("Sorry, I didn't understand that command. Say help for available commands.")
    
    return True


def show_help():
    """Show available voice commands"""
    speak("Here are some commands you can try")
    print("\n" + "="*60)
    print("📝 AVAILABLE VOICE COMMANDS:")
    print("="*60)
    print("  ⏰ What time is it?")
    print("  📅 What's the date?")
    print("  😂 Tell me a joke")
    print("  🌐 Open Google / Open YouTube")
    print("  🔍 Search Python tutorials")
    print("  📚 Who is Albert Einstein?")
    print("  📚 What is machine learning?")
    print("  ❓ Help (show this list)")
    print("  🚪 Exit / Goodbye (close Igris)")
    print("="*60 + "\n")


# ============================================================================
# SECTION 5: MAIN PROGRAM (Where everything starts)
# ============================================================================

def main():
    """
    Main function to run Igris voice assistant
    
    EXPLANATION FOR YOUR CLASS:
    ---------------------------
    This is the "main loop" of the program.
    
    How it works:
    1. Print welcome message
    2. Greet the user
    3. Enter an infinite loop (while True)
    4. In each loop:
       - Listen to user's voice
       - Process the command
       - Repeat until user says "exit"
    """
    print("\n" + "="*60)
    print("🎤 IGRIS VOICE ASSISTANT - VOICE ENABLED VERSION")
    print("="*60)
    print("\n🎯 HOW IT WORKS:")
    print("  • SPEAK your commands (Igris listens) 🎤")
    print("  • Igris SPEAKS the responses (you listen) 🔊")
    print("  • Uses Google Speech Recognition (NO PyAudio!)")
    print("  • Say 'help' to see all commands")
    print("  • Say 'exit' to quit\n")
    print("="*60 + "\n")
    
    greet_user()
    
    # Keep listening for voice commands
    while True:
        try:
            print("\n" + "-"*60)
            
            # Listen to user's voice and get text
            command = listen_to_voice()
            
            if command:
                # Process the command
                continue_running = process_command(command)
                
                # Exit if user said goodbye
                if not continue_running:
                    break
            
            print("-"*60)
                
        except KeyboardInterrupt:
            print("\n\n⚠️ Interrupted by user")
            speak("Shutting down. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            speak("Sorry, something went wrong. Let's try again.")
    
    print("\n" + "="*60)
    print("✅ Igris has shut down. Goodbye!")
    print("="*60 + "\n")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    This is where Python starts running the program
    __name__ == "__main__" means this file is being run directly
    (not imported as a module)
    """
    main()
