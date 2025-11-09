** start of main.py **

def favorite_songs(playlist):
    top = 0
    top_playlist = []
    top_play_key = ""
    for play in playlist:
        if(play["plays"] > top):
            top = play["plays"]
            top_play_key = play["title"]
    
    top_playlist.append(top_play_key)

    top_two = 0
    for a_play in playlist:
        if(a_play['title'] != top_playlist[0]):
            if(a_play['plays'] > top_two):
                top_two = a_play['plays']
                top_play_key = a_play['title']
    
    top_playlist.append(top_play_key)

    return top_playlist

** end of main.py **

