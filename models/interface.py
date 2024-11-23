__options = {
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
    'music_library':[
        'Search',
        'Select',
        'Play',
        "Create Track"
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
}
def Menu(interface:str):
    count = 0
    if interface in __options:
        for choice in __options[interface]:
            count += 1
            print(f'[{count}] {choice}')

def prompt(string:str, type=str):
    initial = input(string)
    if initial == '':
        print(f"User input cannot be empty")
        return prompt(string, type)

    if type is int:
        try:
            int(initial)
        except ValueError as err:
            print(f"Error: {err}")
            return prompt(string, type)

prompt("Enter anything: ", type=int)