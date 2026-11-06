2"""
Igris - Simple Voice Assistant (PyAudio-Free Version)
A beginner-friendly voice assistant for learning Python
Works on Python 3.14+ without PyAudio compilation issues!
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyjokes
import wikipedia
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time

def speak(text):
    """Convert text to speech - creates fresh engine to avoid sounddevice conflicts"""
    print(f"Igris: {text}")
    try:
        # Create a fresh engine instance to avoid conflicts with sounddevice
        engine = pyttsx3.init()
        
        # Configure engine
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        
        # Speak the text
        engine.say(text)
        engine.runAndWait()
        
        # Cleanup
        engine.stop()
        del engine
        
    except Exception as e:
        print(f"⚠️ TTS Error: {e}")


def listen():
    """Listen to user's voice command and convert to text - PyAudio-FREE!"""
    recognizer = sr.Recognizer()
    
    try:
        print("\n🎤 Listening... (Speak now - you have 15 seconds)")
        
        # Recording parameters
        fs = 44100  # Sample rate
        seconds = 15  # Duration - plenty of time to speak!
        
        # Record audio using sounddevice (no PyAudio needed!)
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        
        # Give audio device time to fully release before TTS uses it
        time.sleep(0.5)
        
        # Save to WAV file
        write("temp_voice.wav", fs, recording)
        print("🔄 Recognizing...")
        
        # Use SpeechRecognition to process the WAV file
        with sr.AudioFile("temp_voice.wav") as source:
            audio = recognizer.record(source)
        
        # Convert speech to text using Google Speech Recognition
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"✅ You said: {command}")
        return command.lower()
        
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        speak("Sorry, I didn't catch that. Please speak again.")
        return "none"
    except sr.RequestError:
        speak("Sorry, my speech service is down. Check your internet connection.")
        return "none"
    except Exception as e:
        print(f"❌ Microphone error: {e}")
        # Raise the exception so main loop can count consecutive errors
        raise Exception(f"Microphone access failed: {e}")


def listen_text():
    """Get user command via keyboard input"""
    try:
        command = input("\n⌨️  Type your command: ").strip()
        if command:
            print(f"✅ You typed: {command}")
            return command.lower()
        else:
            return "none"
    except Exception as e:
        print(f"❌ Input error: {e}")
        return "none"


def greet_user():
    """Greet the user based on time of day"""
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Igris, your voice assistant. How may I help you?")


def tell_time():
    """Tell the current time"""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")


def tell_date():
    """Tell the current date"""
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today is {current_date}")


def tell_joke():
    """Tell a random joke"""
    joke = pyjokes.get_joke()
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
        'instagram': 'https://www.instagram.com'
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
        # Get 2 sentences summary from Wikipedia
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any results on Wikipedia.")
    except:
        speak("Sorry, something went wrong with Wikipedia search.")


def process_command(command):
    """Process the user's command and take appropriate action"""
    
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
    elif 'open facebook' in command:
        open_website('facebook')
    elif 'open instagram' in command:
        open_website('instagram')
    
    # Search Google
    elif 'search' in command or 'google' in command:
        # Remove trigger words to get the search query
        search_query = command.replace('search', '').replace('google', '').replace('for', '').strip()
        if search_query:
            search_google(search_query)
        else:
            speak("What should I search for?")
    
    # Wikipedia search
    elif 'wikipedia' in command or 'who is' in command or 'what is' in command:
        # Extract the search query
        search_query = command.replace('wikipedia', '').replace('who is', '').replace('what is', '').strip()
        if search_query:
            search_wikipedia(search_query)
        else:
            speak("What should I search on Wikipedia?")
    
    # Exit commands
    elif 'exit' in command or 'quit' in command or 'bye' in command or 'goodbye' in command:
        speak("Goodbye! Have a great day!")
        return False
    
    # Unknown command
    else:
        speak("Sorry, I didn't understand that command. Please try again.")
    
    return True


def main():
    """Main function to run Igris voice assistant"""
    print("=" * 60)
    print("🤖 IGRIS VOICE ASSISTANT - PyAudio-Free Version")
    print("=" * 60)
    
    # Let user choose input mode
    print("\n🎯 SELECT INPUT MODE:")
    print("  1 - Text Input (Keyboard)")
    print("  2 - Voice Input (Microphone)")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            input_mode = "text"
            print("\n✅ Text Input Mode Selected")
            print("\n📝 TIPS:")
            print("  • Type your commands when prompted")
            print("  • Type 'Exit' or 'Goodbye' to quit")
            print("  • Press Ctrl+C to force stop\n")
            break
        elif choice == "2":
            input_mode = "voice"
            print("\n✅ Voice Input Mode Selected")
            print("\n📝 TIPS:")
            print("  • Speak clearly when 'Listening...' appears")
            print("  • You have 15 seconds to speak")
            print("  • Say 'Exit' or 'Goodbye' to quit")
            print("  • Press Ctrl+C to force stop\n")
            break
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")
    
    print("=" * 60 + "\n")
    
    greet_user()
    
    # Track consecutive errors to prevent infinite loops
    consecutive_errors = 0
    max_consecutive_errors = 3
    
    # Keep listening for commands
    while True:
        try:
            # Use the selected input mode
            if input_mode == "text":
                command = listen_text()
            else:  # voice mode
                command = listen()
            
            # Reset error counter on successful listen
            consecutive_errors = 0
            
            if command != "none":
                # Process the command
                continue_running = process_command(command)
                
                # Exit if user said goodbye
                if not continue_running:
                    break
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            speak("Shutting down. Goodbye!")
            break
        except Exception as e:
            consecutive_errors += 1
            print(f"❌ Error: {e}")
            print(f"⚠️  Consecutive errors: {consecutive_errors}/{max_consecutive_errors}")
            
            if consecutive_errors >= max_consecutive_errors:
                print("\n🛑 Too many consecutive errors. Shutting down for safety.")
                speak("I'm experiencing repeated errors. Shutting down now. Please check your microphone and internet connection, then try again.")
                break
            else:
                speak("Sorry, something went wrong. Let's try again.")


if __name__ == "__main__":
    main()
