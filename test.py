from models import Playlist,MusicLibrary, Track, Queue
from models.track.initializedTracks import *
p = Playlist("nice")
m = MusicLibrary()
# t1 = Track('Blinding Lights', 'The Weeknd', 'After Hours', Duration(minute=3, sec=20))

print(t2.__str__(mode="full"))
for track in listofTracks:
    p.insert(track)
q = Queue(p.inorder(m.root))
# for i  in range(1):
#     q.next()
print(p)
print(q)
    