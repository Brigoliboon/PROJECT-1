from models import MusicLibrary, ArrayList
from datetime import datetime
from abc import ABC, abstractmethod
class Database(ABC):
    def __init__(self) -> None:
        self.__currentDate = datetime.now()

    @abstractmethod
    def save(self):
        pass

    def updatedate(self):
        pass
    
    def updateSize(self):
        pass

class MusiclibDB(Database):  
    def save(obj:MusicLibrary)-> None:
        pass