from ..models.avltree.trackavltree import MusicLibrary
from ..models.Playlist.initializedTracks import listofTracks
m = MusicLibrary()
for track in listofTracks:
    m.insert(track)

print(m.inorder(m.getRoot()))