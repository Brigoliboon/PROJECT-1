from models import MusicLibrary, ArrayList
from datetime import datetime
from . import __database__, __DB_path__
from abc import ABC, abstractmethod
import pickle
import base64
import csv

class Database(ABC):
    def __init__(self) -> None:
        self.__currentDate = datetime.now()
    
    def currentdate(self):
        return self.__currentDate
    @abstractmethod
    def save(self):
        pass

    @staticmethod
    def objtobs64(obj:object):
        byte = pickle.dumps(obj)
        return base64.b64encode(byte).decode("utf-8")
    
    @staticmethod
    def write():
        with open(__DB_path__, 'w') as f:
            f.write(csv.writer(__database__))
      
class MusiclibDB(Database):  
    def save(self, obj:MusicLibrary)-> None:
        b64 = self.objtobs64(obj)
        __database__[0] = ["MusicLibrary",obj.getSize() ,b64, self.currentdate()]
        self.write()

class PLList(Database):
    def save(self, obj:ArrayList)-> None:
        b64 = self.objtobs64(obj)
        __database__[1] = ["PlaylistList",obj.getSize() ,b64, self.currentdate()]
        self.write()

class AlbumList(Database):
    def save(self, obj:ArrayList)-> None:
        b64 = self.objtobs64(obj)
        __database__[2] = ["PlaylistList",obj.getSize() ,b64, self.currentdate()]
        self.write()