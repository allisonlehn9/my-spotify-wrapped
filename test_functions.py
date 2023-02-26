import spotify_functions

def test_suite():
    try:
        spotify_functions.generate_token()
    except:
        return "Default token error"
    try:
        spotify_functions.get_track_id("The Louvre")
    except:
        return "Track ID function failed"
    try:
        spotify_functions.get_top_artists()
    except:
        return "Top artists function failed"
    try:
        spotify_functions.top_artist_names(limit=5,offset=5)
    except:
        return "Top artists names function failed"

test_suite()