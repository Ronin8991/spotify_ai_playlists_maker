import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from saved_tracks_extractor import get_genres

# Function to initialize the Spotify API client
def initialize_spotify():
    load_dotenv()  # Load environment variables from .env file
    scope = "user-library-read playlist-modify-public"  # Define the scope of access
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))  # Return the Spotify client

# Function to retrieve track data from the user's saved tracks
def get_track_data(sp, total_tracks=60, batch_size=20):
    track_data = {}  # Initialize an empty dictionary to hold track data
    for offset in range(0, total_tracks, batch_size):  # Loop through the total tracks in batches
        tracks = sp.current_user_saved_tracks(limit=batch_size, offset=offset)  # Get a batch of saved tracks
        track_ids = [item['track']['id'] for item in tracks['items']]  # Extract track IDs from the response
        track_data_batch = get_genres(track_ids, sp)  # Get genres for the batch of track IDs
        
        if offset == 0:  # If it's the first batch, initialize track_data
            track_data = track_data_batch
        else:  # For subsequent batches, append the data
            for key in track_data:
                track_data[key] += track_data_batch[key]
    
    return track_data  # Return the collected track data

# Function to create a dictionary mapping track IDs to their genres
def create_genre_dict(track_data):
    return dict(zip(track_data['id'], track_data['genres']))  # Zip track IDs with their genres

# Function to create a unique list of genres from the genre dictionary
def create_genre_list(genre_dict):
    genre_list = []  # Initialize an empty list for genres
    for genres in genre_dict.values():  # Iterate through the genres in the dictionary
        for genre in genres:
            if genre not in genre_list:  # Add genre if it's not already in the list
                genre_list.append(genre)
    genre_list.append('no genre')  # Add a 'no genre' category
    return genre_list  # Return the list of unique genres

# Function to create a dictionary of playlists categorized by genre
def create_playlist_dict(genre_dict, genre_list):
    playlist_dict = {genre: [] for genre in genre_list}  # Initialize a dictionary for playlists
    for song, genres in genre_dict.items():  # Iterate through songs and their genres
        if not genres:  # If no genres, add to 'no genre' playlist
            playlist_dict['no genre'].append(song)
        else:  # Otherwise, add to the respective genre playlists
            for genre in genres:
                if song not in playlist_dict[genre]:  # Avoid duplicates in the playlist
                    playlist_dict[genre].append(song)
    return playlist_dict  # Return the dictionary of playlists

# Function to retrieve all playlists of a user
def get_user_playlists(sp, target_user_id, batch_size=50):
    user_playlists = []  # Initialize an empty list for user playlists
    for offset in range(0, 9000, batch_size):  # Loop through user playlists in batches
        user_playlists_batch = sp.user_playlists(user=target_user_id, limit=batch_size, offset=offset)  # Get a batch of playlists
        user_playlists += user_playlists_batch["items"]  # Append the batch to the user playlists list
        if len(user_playlists_batch["items"]) < batch_size:  # Break if there are no more playlists
            break
    return user_playlists  # Return the list of user playlists

# Function to create and populate genre-based playlists for the user
def create_genre_playlists(sp, target_user_id, playlist_dict, user_playlists):
    for genre, songs in playlist_dict.items():  # Iterate through each genre and its songs
        # Unfollow existing playlist with the same name
        for playlist in user_playlists:
            if playlist['name'] == genre:  # Check if a playlist with the same name exists
                sp.user_playlist_unfollow(user=target_user_id, playlist_id=playlist['id'])  # Unfollow the existing playlist 
        
        # Create new playlist
        playlist_created = sp.user_playlist_create(user=target_user_id, name=genre, public=True, collaborative=False, description='')  # Create a new playlist
        
        # Add songs to the playlist
        sp.user_playlist_add_tracks(user=target_user_id, playlist_id=playlist_created['id'], tracks=songs)  # Add songs to the newly created playlist

# Main function to execute the script
def main():
    sp = initialize_spotify()  # Initialize the Spotify client
    target_user_id = '31ighcy6cpa3jsteh7imcasje2ea'  # Define the target user ID
    # create a folder for the user
    os.makedirs(f'{target_user_id}', exist_ok=True)
    
    genre_maker = True
    if genre_maker: 
        track_data = get_track_data(sp)  # Get track data
        genre_dict = create_genre_dict(track_data)  # Create a dictionary of genres
        genre_list = create_genre_list(genre_dict)  # Create a list of unique genres
        playlist_dict = create_playlist_dict(genre_dict, genre_list)  # Create a dictionary of playlists by genre
        user_playlists = get_user_playlists(sp, target_user_id)  # Retrieve user playlists
        create_genre_playlists(sp, target_user_id, playlist_dict, user_playlists)  # Create genre-based playlists
    

if __name__ == "__main__":
    main()  # Execute the main function