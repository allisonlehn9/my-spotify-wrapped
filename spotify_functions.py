import spotipy
import requests
import numpy
import spotipy.util as util

USERNAME = '[insert username]'
CLIENT_ID ='[insert client id]'
CLIENT_SECRET = '[insert client secret]'
REDIRECT_URI = '[insert redirect uri]'
SCOPE = None

def generate_token(username=USERNAME, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE):
    '''
    Creates a bearer token for use with the following Spotify API functions. 
    Allows specification of the scope within the particular functions as they are necessary.

    username : str
    client_id : str
    client_secret : str
    redirect_uri : str
    scope : str (default None)
    '''
    return util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)


### Functions that return JSON output

def get_track_id(track_name: str):
    '''
    Retrieves the Spotify track id numbers returned from querying the title of a song. 
    
    track_name : str
    '''
    token = generate_token() # no special scope necessary for this function
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    params = [
    ('q', track_name),
    ('type', 'track'),
    ]
    try:
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 5)
        return response.json()
    except:
        return None

def get_top_artists(limit = 50, offset = 0, time_range = 'medium_term'):
    '''
    Returns a JSON response object with a user's top spotify artist information.
    
    limit : int, max value is 50
    offset : int, use to get songs beyond the limit
    time_range: 'short_term' (approximately last 4 weeks), 
                'medium_term' (approximately last 6 months), 
                'long_term' (calculated from several years of data and including
                                all new data as it becomes available)
    '''
    token = generate_token(scope="user-top-read") # need specific scope to access user data
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    params = [
        ('limit', limit),
        ('offset', offset),
        ('time_range', time_range)
    ]
    try:
        response = requests.get('https://api.spotify.com/v1/me/top/artists', 
                    headers = headers, params = params)
        return response.json()
    except:
        return None

### Functions that manipulate JSON output

def top_artist_names(limit = 50, offset = 0, time_range = 'medium_term'):
    '''
    Prints a list of all of the names of the top artists in the specified range.
    '''
    json_response = get_top_artists(limit, offset, time_range)
    i = offset
    for item in json_response['items']:
        i += 1
        print(f'{i}. {item["name"]} : {item["popularity"]}')

