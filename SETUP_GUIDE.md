# 🚀 Setup Guide - Igris Voice Assistant

## Step-by-Step Installation (For Complete Beginners)

### Step 1: Check Python Installation
First, make sure you have Python installed.

Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux) and type:
```bash
python --version
```

You should see something like: `Python 3.8.0` or higher

If not, download Python from: https://www.python.org/downloads/

---

### Step 2: Navigate to Your Project Folder

Open Command Prompt and navigate to your project folder:
```bash
cd "E:\Python Project"
```

---

### Step 3: Install Required Libraries

Run this command to install all necessary libraries:
```bash
pip install SpeechRecognition pyttsx3 wikipedia
```

**What this does:**
- `SpeechRecognition` - For listening to your voice
- `pyttsx3` - For speaking responses
- `wikipedia` - For Wikipedia searches

---

### Step 4: Test the Keyboard Version First

This helps verify everything is working:
```bash
python igris_keyboard.py
```

If this works, you're ready for the voice version!

---

### Step 5: Run the Voice Version

```bash
python igris_voice.py
```

**Make sure:**
- ✅ Your microphone is connected
- ✅ You have internet connection (for Google Speech API)
- ✅ Microphone permissions are enabled

---

## 🔧 Troubleshooting

### Problem 1: "No module named 'speech_recognition'"
**Solution:**
```bash
pip install SpeechRecognition
```

---

### Problem 2: "Microphone not found"
**Solution:**
- Check if microphone is connected
- On Windows: Settings → Privacy → Microphone → Allow apps to access microphone
- Try running as administrator

---

### Problem 3: "OSError: [Errno -9996] Invalid input device"
**Solution:**
- This might mean you DO need PyAudio for microphone access
- Try installing it:
```bash
pip install pipwin
pipwin install pyaudio
```

Or on some systems:
```bash
pip install pyaudio
```

If that fails, try:
```bash
# Download the appropriate .whl file for your Python version from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Then install it with:
pip install path/to/downloaded/file.whl
```

---

### Problem 4: "RequestError - No internet connection"
**Solution:**
- The voice version needs internet for Google Speech API
- Check your internet connection
- Try the keyboard version (works offline)

---

### Problem 5: "pyttsx3 not speaking"
**Solution:**
Windows users - try this:
```python
# In the code, change:
engine.setProperty('voice', voices[1].id)  # Try voice[1] instead of voice[0]
```

---

## 📋 Quick Test Checklist

Before presenting, test these commands:

### Keyboard Version Tests:
- [ ] "what time is it"
- [ ] "tell me a joke"
- [ ] "open google"
- [ ] "search python tutorials"
- [ ] "help"
- [ ] "exit"

### Voice Version Tests:
- [ ] Say: "What time is it?"
- [ ] Say: "Tell me a joke"
- [ ] Say: "Open YouTube"
- [ ] Say: "Who is Albert Einstein?"
- [ ] Say: "Help"
- [ ] Say: "Exit"

---

## 🎤 Microphone Tips for Better Recognition

1. **Speak Clearly**
   - Don't speak too fast or too slow
   - Use normal conversational tone

2. **Reduce Background Noise**
   - Close windows
   - Turn off fans/AC when testing
   - Choose a quiet room

3. **Microphone Position**
   - Keep mic 6-12 inches from your mouth
   - Don't cover the microphone
   - Use a good quality microphone if possible

4. **Test Your Microphone**
   - Windows: Settings → System → Sound → Test your microphone
   - Make sure levels are appropriate (not too quiet, not too loud)

---

## 🎯 Ready for Presentation?

### Before your demo:
1. ✅ Test both versions work
2. ✅ Prepare 3-4 example commands to demonstrate
3. ✅ Have backup (show keyboard version if voice fails)
4. ✅ Read VOICE_EXPLANATION.md to understand concepts
5. ✅ Practice explaining the "no PyAudio" approach

### During presentation:
1. Show keyboard version first (simpler)
2. Explain the challenge (PyAudio problems)
3. Demo voice version (impressive!)
4. Explain your solution (Google API)
5. Take questions confidently!

---

## 📞 Still Having Issues?

Common quick fixes:
```bash
# Reinstall everything fresh
pip uninstall SpeechRecognition pyttsx3 wikipedia
pip install SpeechRecognition pyttsx3 wikipedia

# Update pip first
python -m pip install --upgrade pip

# Try with admin rights (Windows)
# Right-click Command Prompt → Run as Administrator
```

---

## 🌟 You're Ready!

Once everything works, you have:
- ✅ A working voice assistant
- ✅ Clean, well-commented code
- ✅ Understanding of speech recognition
- ✅ A PyAudio-free solution
- ✅ Great project to demonstrate!

Good luck with your presentation! 🎉
