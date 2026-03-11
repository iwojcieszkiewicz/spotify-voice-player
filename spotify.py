import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

load_dotenv()
class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                redirect_uri=os.getenv("REDIRECT_URI"),
                scope="user-modify-playback-state user-read-playback-state playlist-read-private playlist-read-collaborative"
            ))

    def play_song(self, query):
        results = self.sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            uri = track['uri']
            name = track['name']
            artist = track['artists'][0]['name']

            self.sp.start_playback(uris=[uri])
            print(f"Odtwarzam: {artist} - {name}")

    def start_song(self):
        self.sp.start_playback()
        print("Wznowiono")

    def pause_song(self):
        self.sp.pause_playback()
        print("Zatrzymano")

    def next_song(self):
        self.sp.next_track(self)
        print("Puszczono następną piosenkę")

    def previous_track(self):
        self.sp.previous_track()
        print("Puszczono poprzednią piosenkę")

    def get_my_playlists_uri(self):
        playlists = self.sp.current_user_playlists()
        print("Twoje playlisty:")
        for i, pl in enumerate(playlists['items']):
            print(f"{i+1}. {pl['name']}")
        return playlists['items'][1]

    def play_playlist(self):
        self.sp.start_playback(context_uri='spotify:playlist:28foiMOcX3EROacW86X3go')
