options = {
    "MAIN":[
        "Enter Music Library",
        "View List of Playlists",
        "Create Playlist",
        "View Albums",
        "Exit"
    ],
    'track':[
        'Add to a Playlist',#more
        'Delete',
        "Exit",
    ],
    'musiclibrary':[
        'Search',
        'Select',
        'Play',
        "Create Track",
        'Next Page',
        'Previous Page',
        'Exit'
        ],
    "playlist-internal":[
        "Play",
        "Next Page",
        "Previous Page",
        "Exit"
    ],
    "playlist-external":[
        "Select Playlist",
        "Next Page",
        "Previous Page",
        "Exit"
    ],
    "queue":[
        "{}",
        "Next",
        "Previous",
        "Turn {} Repeat"
        "Turn {} Repeat"
    ]
}
def Menu(interface:str):
    count = 0
    if interface in options:
        for choice in options[interface]:
            count += 1
            print(f'[{count}] {choice}')

def prompt(string:str, type=str|int)->int|str:
    assert type is str or type is int, 'type must only be int or str' 
    initial = input(string)
    if initial == '':
        print(f"User input cannot be empty")
        return prompt(string, type)
    try:
        initial = type(initial)
    except ValueError as err:
        print(f"Error: {err}")
        return prompt(string, type)
    return initial