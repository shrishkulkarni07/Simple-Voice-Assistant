"""
Igris - Keyboard Version (FIXED TTS)
A beginner-friendly voice assistant that uses KEYBOARD INPUT
You TYPE commands, Igris SPEAKS responses!
No PyAudio needed - works immediately!
"""

import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize the text-to-speech engine
def get_engine():
    """Get a fresh TTS engine instance"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    return engine


def speak(text):
    """Convert text to speech - GUARANTEED to work"""
    print(f"🔊 Igris: {text}")
    try:
        # Create fresh engine for each speak (fixes Windows TTS issues)
        engine = get_engine()
        engine.say(str(text))
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"⚠️ Speech error: {e}")


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
    speak("Type your commands and I'll speak the responses!")


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
    # Use simple built-in jokes (no pyjokes dependency issues)
    import random
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar, walks up to two tables and asks: Can I join you?",
        "Why do Java developers wear glasses? Because they cannot see sharp!",
        "How many programmers does it take to change a light bulb? None, that is a hardware problem!",
        "Why did the programmer quit his job? Because he did not get arrays!",
        "What is a programmer's favorite hangout place? Foo Bar!",
        "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25!",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "A programmer's wife tells him: Go to the store and pick up a loaf of bread. If they have eggs, get a dozen. The programmer comes home with 12 loaves of bread.",
        "Why did the developer go broke? Because he used up all his cache!"
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
        # Get 2 sentences summary from Wikipedia
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
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
    elif 'open reddit' in command:
        open_website('reddit')
    elif 'open stack overflow' in command:
        open_website('stack overflow')
    
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
    
    # Help command
    elif 'help' in command or 'commands' in command:
        show_help()
    
    # Exit commands
    elif 'exit' in command or 'quit' in command or 'bye' in command or 'goodbye' in command:
        speak("Goodbye! Have a great day!")
        return False
    
    # Unknown command
    else:
        speak("Sorry, I didn't understand that command. Type help for available commands.")
    
    return True


def show_help():
    """Show available commands"""
    speak("Here are some commands you can try")
    print("\n" + "="*60)
    print("📝 AVAILABLE COMMANDS:")
    print("="*60)
    print("  ⏰ what time is it")
    print("  📅 what's the date")
    print("  😂 tell me a joke")
    print("  🌐 open google / open youtube / open github")
    print("  🔍 search python tutorials")
    print("  📚 who is Albert Einstein")
    print("  📚 what is machine learning")
    print("  ❓ help (show this list)")
    print("  🚪 exit / quit / bye (close Igris)")
    print("="*60 + "\n")


def main():
    """Main function to run Igris voice assistant"""
    print("\n" + "="*60)
    print("⌨️  IGRIS VOICE ASSISTANT - KEYBOARD VERSION (FIXED)")
    print("="*60)
    print("\n📝 HOW IT WORKS:")
    print("  • TYPE your commands (you don't speak)")
    print("  • Igris SPEAKS the responses (you listen) 🔊")
    print("  • No microphone needed!")
    print("  • Type 'help' to see all commands")
    print("  • Type 'exit' to quit\n")
    print("="*60 + "\n")
    
    greet_user()
    
    # Keep listening for commands
    while True:
        try:
            # Get keyboard input
            print("\n" + "-"*60)
            command = input("⌨️  Type your command: ").strip().lower()
            print("-"*60)
            
            if command:
                # Process the command
                continue_running = process_command(command)
                
                # Exit if user said goodbye
                if not continue_running:
                    break
            else:
                speak("Please type something!")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            speak("Shutting down. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ ERROR DETAILS: {type(e).__name__}: {e}")
            print(f"   If this keeps happening, please share this error message!")
            speak("Sorry, something went wrong. Let's try again.")
    
    print("\n" + "="*60)
    print("✅ Igris has shut down. Goodbye!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
