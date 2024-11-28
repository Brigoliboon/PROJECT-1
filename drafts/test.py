import pickle
import json
import base64
import sys
sys.path.append('.')
from models import MusicLibrary, ArrayList
m = MusicLibrary()
a = ArrayList()
bytes_data = pickle.dumps(m)

bytetostring = base64.b64encode(bytes_data).decode('utf-8')
print(bytetostring)
# json_data = json.dumps(bytetostring)
# loaded_data = json.loads(json_data)
# loaded_bytes = base64.b64decode(loaded_data)
# reconst = pickle.loads(loaded_bytes)
# print(reconst)