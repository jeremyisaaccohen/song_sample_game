#!/usr/bin/python3

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


username = 'jeremycohen2323'
scope = 'user-library-read'

# token = util.prompt_for_user_token(username, scope)

CID = 'd951d0176e2c4c26b37d547c1421d392'
SECRET = '4783680eb7074cc7bd6af4196de05aea'


client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# print(sp.user('jeremycohen2323'))

hood_shit_playlist = sp.playlist('https://open.spotify.com/playlist/1cuFC7Ohk1c1J9eLokmLfs?si=0232756e630240de')

# tracks = hood_shit_playlist['tracks']

def get_songs_and_artists_from_playlist_id(playlist_id):
    #as a list of tuples
    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']
    all_songs_and_artists = []
    for item in tracks['items']:
        track = item['track']
        artist = track['artists'][0]['name']
        song = track['name']

        song_and_artist = (song,artist)
        # print(song_and_artist, '\n')
        all_songs_and_artists.append(song_and_artist)

    return all_songs_and_artists

        # print(track['artists'][0]['name'], track['name'])


soft = get_songs_and_artists_from_playlist_id('https://open.spotify.com/playlist/1EZ5KdY6eyMRV4YrldSYTL?si=ed9cc1ce262e4b35')
hard = get_songs_and_artists_from_playlist_id('https://open.spotify.com/playlist/1cuFC7Ohk1c1J9eLokmLfs?si=0232756e630240de')

print("SOFT : " , soft)
print("HARD : ", hard)




# if hood_shit_playlist['owner']['id'] == username:
#             print()
#             print(hood_shit_playlist['name'])
#             print('  total tracks', hood_shit_playlist['tracks']['total'])
#             results = sp.user_playlist(username, hood_shit_playlist['id'], fields="tracks,next")
#             tracks = results['tracks']
#             get_songs_and_artists(tracks)
#             while tracks['next']:
#                 tracks = sp.next(tracks)
#                 get_songs_and_artists(tracks)
