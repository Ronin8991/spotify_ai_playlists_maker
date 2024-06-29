## Test creazione automatica di playlist spotify

Per ora ho creato una funziona che a batch prende le miei canzoni salvate e crea un dataframe con le informazioni di ogni canzone, compresi audio features e audio analysis.

### Idee
1. clustering sulla base delle caratteristiche
2. usare Get Recommendations API per creare playlist automatiche, questo metodo accetta molti parametri, capire come usarli, magari partire dalle playlist già esistenti, e poi fare delle modifiche

### TODO
1. creazione di playlist automatiche e salvataggio per testing
2. estrazione di informazioni da playlist già esistenti, 
3. capire come estrarre le playlist mie e come tenere in ordine anche questa informazione, magari aggiungere alla tabella principale una variabile che indica le playlist a cui appartiene la canzone, sotto forma di lista di stringhe

### Rate limit

##### Develop a backoff-retry strategy

When your app has been rate limited it will receive a 429 error response from Spotify. Your app can use this information as a cue to slow down the number of API requests that it makes to the Web API. The header of the 429 response will normally include a Retry-After header with a value in seconds. Consider waiting for the number of seconds specified in Retry-After before your app calls the Web API again.

#### Use batch APIs to your advantage

Spotify has some APIs — like the Get Multiple Albums endpoint — that allow you to fetch a batch of data in one API request. You can reduce your API requests by calling the batch APIs when you know that you will need data from a set of objects.


### Working with playlists
- https://developer.spotify.com/documentation/web-api/concepts/playlists

- To read a playlist, we first need to find it, and for that we need its Spotify ID. The Get a List of a User’s Playlists gives us an easy way to get basic details about a user’s playlists, including their IDs
- Once we have a list of playlists we can retrieve the details of a specific playlist using the Web API’s Get a Playlist endpoint, and a list of its items using Get a Playlist’s Items.

## Librerie trovate
- https://github.com/jayme-github/spotify-backup
- https://github.com/blekmus/spotify-backup