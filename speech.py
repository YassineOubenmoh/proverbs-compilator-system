import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
    audio = recognizer.listen(mic)

try:
    text = recognizer.recognize_google(audio, language="ar-SA")
    print(f"Recognized text: {text.lower()}")
except sr.UnknownValueError:
    print("Speech recognition could not understand audio.")
except sr.RequestError as e:
    print(f"Google Web Speech API request failed; {e}")
