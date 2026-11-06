"""
IGRIS VOICE ASSISTANT - INTERACTIVE VOICE ACTIVATION
This listens to your microphone and responds to voice commands!
"""

import pyttsx3
import speech_recognition as sr
import time
import webbrowser
from datetime import datetime
import random

# Initialize TTS engine once
engine = pyttsx3.init()

def speak(text):
    """Make the computer speak"""
    print(f"\n🔊 Igris: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and convert to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("🔄 Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"✅ You said: \"{text}\"")
            return text.lower()
        except sr.WaitTimeoutError:
            print("⏰ No speech detected. Please try again.")
            return None
        except sr.UnknownValueError:
            print("❓ Could not understand. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech Recognition error: {e}")
            return None

def tell_time():
    """Tell the current time"""
    now = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def tell_date():
    """Tell the current date"""
    today = datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def tell_joke():
    """Tell a random joke"""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the computer cold? It left its Windows open!",
        "What do you call a computer that sings? A-Dell!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "There are only 10 types of people in the world: those who understand binary and those who don't.",
    ]
    speak(random.choice(jokes))

def open_website(site):
    """Open a website in the browser"""
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
    }
    if site in sites:
        speak(f"Opening {site}")
        webbrowser.open(sites[site])
    else:
        speak(f"Sorry, I don't have a link for {site}")

def process_command(command):
    """Process the voice command and execute the appropriate action"""
    if command is None:
        return True  # Continue listening

    if "time" in command:
        tell_time()
    elif "date" in command or "day" in command:
        tell_date()
    elif "joke" in command:
        tell_joke()
    elif "open youtube" in command:
        open_website("youtube")
    elif "open google" in command:
        open_website("google")
    elif "open github" in command:
        open_website("github")
    elif "open instagram" in command:
        open_website("instagram")
    elif "open facebook" in command:
        open_website("facebook")
    elif "your name" in command or "who are you" in command:
        speak("I am Igris, your voice assistant!")
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")
    elif "exit" in command or "quit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        return False  # Stop listening
    else:
        speak("Sorry, I didn't understand that command. Please try again.")

    return True  # Continue listening

def main():
    print("=" * 60)
    print("🎤 IGRIS VOICE ASSISTANT")
    print("=" * 60)
    print("\n� Available Commands:")
    print("   • 'What time is it?'")
    print("   • 'What is today's date?'")
    print("   • 'Tell me a joke'")
    print("   • 'Open YouTube / Google / GitHub / Instagram / Facebook'")
    print("   • 'What is your name?'")
    print("   • 'Hello'")
    print("   • 'Exit' / 'Quit' / 'Stop' / 'Bye' — to quit")
    print("=" * 60)

    speak("Hello! I am Igris, your voice assistant. How can I help you?")

    running = True
    while running:
        command = listen()
        running = process_command(command)

    print("\n" + "=" * 60)
    print("✅ Igris Voice Assistant has been stopped.")
    print("=" * 60)

if __name__ == "__main__":
    main()