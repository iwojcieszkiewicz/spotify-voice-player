import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="f63c43209c4e4019a7e0184c08d4f322",
    client_secret="b59d2c5bee5a4c20be8bccf6c00ce8e0",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

def play_song(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        uri = track['uri']
        name = track['name']
        artist = track['artists'][0]['name']

        sp.start_playback(uris=[uri])
        print(f"Odtwarzam: {artist} - {name}")

def start_song():
    sp.start_playback()
    print("Wznowiono")

def pause_song():
    sp.pause_playback()
    print("Zatrzymano")

def next_song():
    sp.next_track()
    print("Puszczono następną piosenkę")

def previous_track():
    sp.previous_track()
    print("Puszczono poprzednią piosenkę")