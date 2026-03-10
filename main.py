import speech_recognition as sr
from spotify import play_song, pause_song, start_song, next_song, previous_track, play_playlist
from pynput import keyboard

recognizer = sr.Recognizer()

# play_playlist()

def on_press(key):
    try:
        if key.char == "l":
            with sr.Microphone() as source:
                print("Mów...")
                audio = recognizer.listen(source)

            try:
                text:str = recognizer.recognize_google(audio, language="pl-PL")
                print(f"Rozpoznano: {text}")
                if text == "wyjdź":
                    return
                elif "stop" in text.lower():
                    pause_song()
                elif "wznów" in text.lower():
                    start_song()
                elif "następna" in text.lower():
                    next_song()
                elif "poprzednia" in text.lower():
                    previous_track()
                elif "playlista" in text.lower():
                    play_playlist()
                elif "play" in text.lower():
                    song = text[4:]
                    play_song(song)
            except sr.UnknownValueError:
                print("Nie rozpoznano mowy")
            except sr.RequestError as e:
                print(f"Błąd usługi: {e}")
    except AttributeError:
        print(f"Wciśnięto specjalny klawisz: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()