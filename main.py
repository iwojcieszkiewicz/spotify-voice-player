import speech_recognition as sr
from spotify import play_song, pause_song, start_song, next_song, previous_track
from pynput import keyboard

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Mów...")
        audio = recognizer.listen(source)

    try:
        text:str = recognizer.recognize_google(audio, language="pl-PL")
        print(f"Rozpoznano: {text}")
        if text == "wyjdź":
            break
        elif "play" in text.lower():
            song = text[4:]
            play_song(song)
        elif "stop" in text.lower():
            pause_song()
        elif "wznów" in text.lower():
            start_song()
        elif "następna" in text.lower():
            next_song()
        elif "poprzednia" in text.lower():
            previous_track()
    except sr.UnknownValueError:
        print("Nie rozpoznano mowy")
    except sr.RequestError as e:
        print(f"Błąd usługi: {e}")