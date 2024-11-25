from ..models.avltree.trackavltree import MusicLibrary
from ..models.track.initializedTracks import listofTracks
m = MusicLibrary()
for track in listofTracks:
    m.insert(track)

print(m.inorder(m.getRoot()))