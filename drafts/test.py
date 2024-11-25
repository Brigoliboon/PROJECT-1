import pickle
import json
import base64

class s:
    pass

bytes_data = pickle.dumps(s)

bytetostring = base64.b64encode(bytes_data).decode('utf-8')

json_data = json.dumps(bytetostring)
loaded_data = json.loads(json_data)
loaded_bytes = base64.b64decode(loaded_data)
reconst = pickle.loads(loaded_bytes)
print(reconst)