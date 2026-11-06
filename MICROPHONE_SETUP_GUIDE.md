# 🎤 Microphone Setup Guide for Igris Voice Assistant

## ❗ Current Issue

**PyAudio is not available for Python 3.14 yet.** This is why the microphone isn't working.

## ✅ Two Solutions to Run Igris

### **Option 1: Use Python 3.13 (Recommended - Easiest)**

PyAudio has official wheels for Python 3.13. Here's how to set it up:

1. **Download Python 3.13** from [python.org](https://www.python.org/downloads/)
2. **Install it** (make sure to check "Add to PATH")
3. **Open a new terminal** and navigate to your project:
   ```bash
   cd "e:\Python Project"
   ```
4. **Create a virtual environment with Python 3.13:**
   ```bash
   py -3.13 -m venv venv313
   venv313\Scripts\activate
   ```
5. **Install requirements:**
   ```bash
   pip install SpeechRecognition==3.10.1 pyttsx3==2.90 wikipedia==1.4.0 PyAudio
   ```
6. **Run Igris:**
   ```bash
   python igris.py
   ```

---

### **Option 2: Use Keyboard Input Version (Works Now!)**

I see you already have `igris_voice.py` - you can use the keyboard input version which works perfectly without microphone:

**Run this command:**
```bash
python igris_voice.py
```

Then type your commands instead of speaking. For example:
- Type: `what time is it`
- Type: `tell me a joke`
- Type: `open youtube`
- Type: `exit` to quit

---

## 📝 The Fix You Already Have

The infinite loop error **IS FIXED** in `igris.py`! The program now:

✅ Counts consecutive errors  
✅ Stops after 3 failed microphone attempts  
✅ Shows helpful error messages  
✅ Exits gracefully instead of looping forever  

The only remaining issue is **PyAudio installation**, which is a Python version compatibility issue, not a code problem.

---

## 🚀 Quick Test - Run Keyboard Version Now

Want to test Igris right away? Use the keyboard version:

```bash
python igris_voice.py
```

This will work immediately and you can demonstrate all the features!
