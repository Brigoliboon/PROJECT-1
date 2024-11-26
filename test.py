from models import Playlist, Track, Duration
from models.track.initializedTracks import *
p = Playlist("nice")
t1 = Track('Blinding Lights', 'The Weeknd', 'After Hours', Duration(minute=3, sec=20))
p.insert(t1)
p.insert(t3)
p.insert(t4)
print(p.inorder(p.root))
print(p)