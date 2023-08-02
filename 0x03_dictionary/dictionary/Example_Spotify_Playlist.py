# Example on dictionary using nested list
playlist = {
    'title': 'samuel',
    'autor': '3eead',
    'song': [
        {'title': 'samuel', 'artist': ['blue'], 'duration':2.5},
        {'title': 'samueeel', 'artist': ['beelue'], 'duration':2.5},
        {'title': 'samunknel', 'artist': ['bluhje'], 'duration':6.5}
    ]
}

# claculate total lenght of song
total_lenght = 0
for song in playlist['song']:
    total_lenght += song['duration']
print(total_lenght)
