from models import MusicLibrary, ArrayList
from datetime import datetime
from . import __database__, __DB_path__
from .load import database
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
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @staticmethod
    def objtobs64(obj:object):
        byte = pickle.dumps(obj)
        return base64.b64encode(byte).decode("utf-8")
    
    @staticmethod
    def saveDB():
        with open(__DB_path__, 'w') as f:
            f.write(csv.writer(__database__))
    
class MusiclibDB(Database): 
    def load(self):
        return database('MusicLibrary', filter=True) 
    
    def save(self, obj:MusicLibrary)-> None:
        b64 = self.objtobs64(obj)
        __database__[0] = ["MusicLibrary",obj.getSize() ,b64, self.currentdate()]

class PLList(Database):
    def load(self):
        return database('PlaylistList', filter=True)
    
    def save(self, obj:ArrayList)-> None:
        b64 = self.objtobs64(obj)
        __database__[1] = ["PlaylistList",obj.getSize() ,b64, self.currentdate()]

class AlbumList(Database):
    def load(self):
        return database('AlbumList', filter=True)
    
    def save(self, obj:ArrayList)-> None:
        b64 = self.objtobs64(obj)
        __database__[2] = ["PlaylistList",obj.getSize() ,b64, self.currentdate()]
