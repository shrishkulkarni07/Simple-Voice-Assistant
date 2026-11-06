# 🚀 How to Run Igris - Complete Beginner's Guide

## ✅ Installation Status

**Already Installed:**
- ✅ Python 3.14.0
- ✅ SpeechRecognition
- ✅ pyttsx3
- ✅ wikipedia
- ✅ pyjokes

**Needs Installation:**
- ⏳ PyAudio (for microphone input)

---

## 🎯 Quick Start (3 Methods)

### **Method 1: Run Without PyAudio (Simplest - Try This First!)**

You can actually test if the text-to-speech part works without PyAudio. Let's create a simple test:

1. Open PowerShell or Command Prompt in `E:\Python Project`
2. Run this command:

```bash
python igris.py
```

**What will happen:**
- ✅ Text-to-speech will work (you'll hear Igris speak)
- ❌ Voice recognition won't work (can't listen to you)

If you see an error about PyAudio, that's expected! Read Method 2 below to fix it.

---

### **Method 2: Install PyAudio Properly (Recommended)**

PyAudio needs special installation on Windows. Here's the easiest way:

#### **Step 1:** Download Pre-built PyAudio

Visit this website and download the `.whl` file for Python 3.14 on Windows:
- **Link:** https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- **Look for:** `PyAudio‑0.2.14‑cp314‑cp314‑win_amd64.whl` (for 64-bit Windows)
- **Or:** `PyAudio‑0.2.14‑cp314‑cp314‑win32.whl` (for 32-bit Windows)

> **Note:** If you can't find Python 3.14 version, try Python 3.13 or 3.12 version instead.

#### **Step 2:** Install the Downloaded File

After downloading, run this command (replace with your actual filename):

```bash
pip install "C:\Users\shris\Downloads\PyAudio-0.2.14-cp314-cp314-win_amd64.whl"
```

#### **Step 3:** Run Igris

```bash
python igris.py
```

---

### **Method 3: Use Alternative Libraries (For Advanced Users)**

If PyAudio continues to give issues, you can modify the code to use alternative libraries like `sounddevice` instead.

---

## 🎤 How to Use Igris Once Running

### **When You Run the Script:**

1. **Greets You:**
   - Igris will say "Good Morning/Afternoon/Evening"
   - Then: "I am Igris, your voice assistant. How may I help you?"

2. **Listens for Commands:**
   - You'll see: `Listening...`
   - Speak clearly into your microphone
   - You'll see: `Recognizing...`
   - Then: `You said: [your command]`

3. **Responds:**
   - Igris will perform the action
   - Speaks the response

### **Example Commands to Try:**

| Say This | Igris Does This |
|----------|----------------|
| "What time is it?" | Tells current time |
| "What's the date?" | Tells current date |
| "Tell me a joke" | Tells a programming joke |
| "Open Google" | Opens Google in browser |
| "Open YouTube" | Opens YouTube |
| "Search for Python tutorials" | Searches Google |
| "Who is Albert Einstein?" | Searches Wikipedia |
| "Exit" or "Goodbye" | Closes Igris |

---

## 🐛 Troubleshooting

### **Error: "No module named 'pyaudio'"**

**Solution:** Follow Method 2 above to install PyAudio properly.

### **Error: "No module named 'speech_recognition'"**

**Solution:** Run:
```bash
pip install SpeechRecognition
```

### **Microphone Not Working**

**Check:**
1. Is your microphone plugged in?
2. Go to Windows Settings → Privacy → Microphone
3. Make sure microphone access is enabled for apps

### **"Could not understand audio"**

**Tips:**
- Speak louder and clearer
- Reduce background noise
- Wait for "Listening..." before speaking
- Speak close to the microphone

### **"Speech service is down"**

**Solution:**
- Check your internet connection
- Google Speech Recognition needs internet

---

## 📝 Step-by-Step First Run

### **Complete Process:**

1. **Open PowerShell/Command Prompt**
   - Press `Windows + R`
   - Type `powershell`
   - Press Enter

2. **Navigate to Project Folder**
   ```bash
   cd "E:\Python Project"
   ```

3. **Check Python Version**
   ```bash
   python --version
   ```
   Should show: `Python 3.14.0` ✅

4. **Install PyAudio** (if not done)
   - Follow Method 2 above

5. **Run Igris**
   ```bash
   python igris.py
   ```

6. **Test Commands**
   - Wait for "Listening..."
   - Say: "What time is it?"
   - Wait for response

7. **Exit Igris**
   - Say: "Exit" or "Goodbye"
   - Or press `Ctrl + C` to force stop

---

## 🎓 Understanding the Output

When you run `python igris.py`, you'll see:

```
Listening...                    ← Waiting for you to speak
Recognizing...                  ← Converting your speech to text
You said: what time is it      ← What Igris understood
Igris: The time is 11:23 PM    ← Igris's response (also spoken)
Listening...                    ← Ready for next command
```

---

## ⚡ Quick Command Reference

Copy these exact commands in order:

```bash
# Navigate to folder
cd "E:\Python Project"

# Check Python
python --version

# Install dependencies (if needed)
pip install SpeechRecognition pyttsx3 wikipedia pyjokes

# Run Igris
python igris.py
```

---

## 🔧 Alternative: Test Text-to-Speech Only

If you just want to test if the speaking part works, create a simple test file:

**Create:** `test_speak.py`

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello! I am Igris!")
engine.runAndWait()
```

**Run:**
```bash
python test_speak.py
```

This will speak without needing the microphone!

---

## 📞 Need More Help?

If you're still stuck:

1. **Check Python Installation:**
   ```bash
   python --version
   ```

2. **List Installed Packages:**
   ```bash
   pip list
   ```

3. **Reinstall Everything:**
   ```bash
   pip uninstall SpeechRecognition pyttsx3 wikipedia pyjokes
   pip install SpeechRecognition pyttsx3 wikipedia pyjokes
   ```

---

## 🎯 Summary

**Quickest Way to Get Started:**

1. Open PowerShell in `E:\Python Project`
2. Run: `python igris.py`
3. If PyAudio error appears, download and install it from the link in Method 2
4. Run `python igris.py` again
5. Start speaking commands!

**That's it! You're ready to use Igris! 🎉**
