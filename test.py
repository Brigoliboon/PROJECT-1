from database import load
from models import *
import pickle
import base64
r= ArrayList()
d= pickle.dumps(r)
s = base64.b64encode(d).decode("utf-8")
print(s)
# print(load.database("MusicLibrary"))