
def get_genres(track_ids, sp):
    # Maximum 50 track_ids for track info
    track_infos = sp.tracks(track_ids)['tracks']
    
    track_data = {
        'album': [track['album']['name'] for track in track_infos],
        'artist_id': [track['artists'][0]['id'] for track in track_infos],
        'artist': [track['artists'][0]['name'] for track in track_infos],
        'duration_s': [track['duration_ms'] / 1000 for track in track_infos],
        'name': [track['name'] for track in track_infos],
        'popularity': [track['popularity'] for track in track_infos],
        'id': [track['id'] for track in track_infos],
    }
    if len(track_ids)>20:
        print('lenght error')
    # Maximum 20 
    artist_infos = sp.artists(track_data['artist_id'])['artists']
    # print(artist_infos[0]['genres'])
    track_data['genres']=[artist['genres'] for artist in artist_infos]

 
    return track_data




def get_audio_features_and_analysis(track_ids, sp, audio_analysis=False):
    # Maximum 50 track_ids for track info
    track_infos = sp.tracks(track_ids)['tracks']
    
    # Maximum 100 track_ids for audio features
    features = sp.audio_features(track_ids)

    # Maximum 20 
    album_infos = sp.albums([track['album']['id'] for track in track_infos])

    track_data = {
        'album': [track['album']['name'] for track in track_infos],
        'artist': [track['artists'][0]['name'] for track in track_infos],
        'duration_s': [track['duration_ms'] / 1000 for track in track_infos],
        'name': [track['name'] for track in track_infos],
        'popularity': [track['popularity'] for track in track_infos],
        'id': [track['id'] for track in track_infos],
        # audio features
        'acousticness': [feature['acousticness'] for feature in features],
        'danceability': [feature['danceability'] for feature in features],
        'energy': [feature['energy'] for feature in features],
        'instrumentalness': [feature['instrumentalness'] for feature in features],
        'key': [feature['key'] for feature in features],
        'liveness': [feature['liveness'] for feature in features],
        'loudness': [feature['loudness'] for feature in features],
        'mode': [feature['mode'] for feature in features],
        'speechiness': [feature['speechiness'] for feature in features],
        'valence': [feature['valence'] for feature in features],
        'tempo': [feature['tempo'] for feature in features],
        'time_signature': [feature['time_signature'] for feature in features],
    }

    if audio_analysis:
        analyses = [sp.audio_analysis(track['id']) for track in track_infos]
        track_data.update({
            'segments': [len(analysis['segments']) for analysis in analyses],
            'bars': [len(analysis['bars']) for analysis in analyses],
            'beats': [len(analysis['beats']) for analysis in analyses],
            'sections': [len(analysis['sections']) for analysis in analyses],
            'tatums': [len(analysis['tatums']) for analysis in analyses]
        })
    
    return track_data

