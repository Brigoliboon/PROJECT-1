from .duration import Duration
from datetime import datetime, timedelta
class Track:
    def __init__(self, title:str, artist:str,album:str, duration:timedelta) -> None:
        self.__datetimeAdded = datetime.now()
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__duration:timedelta = duration
        self.__occurence = 0
    
    def incrOccurence(self):
        self.__occurence += 1
    
    def decrOccurence(self):
        self.__occurence -= 1
    
    def occurence(self):
        return self.__occurence

    def getDateTime(self):
        return self.__datetimeAdded

    def getTitle(self):
        return self.__title
    
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def getDuration(self):
        return self.__duration
    
    @staticmethod
    def formatduration(time:timedelta, type:str = 'analog'):
        total_sec = time.total_seconds()
        hours = int(total_sec // 3600)
        minutes = int((total_sec % 3600) // 60)
        seconds = int(total_sec % 60)
        match type:
            case 'analog':
                if hours:
                    return f"{hours:02}:{minutes:02}:{seconds:02}"
                else:
                    return f"{minutes:02}:{seconds:02}"
                
            case 'display':
                if hours:
                    return f"{hours:02} hr {minutes:02} min {seconds:02} sec"
                else:
                    return f"{minutes:02} min {seconds:02} sec"
                
    def __str__(self, mode:str = 'prev') -> str:
        if mode == 'prev':
            return f"{self.__title} - {self.__artist} ({self.__duration})"
        elif mode == 'full':
            return f'''
            
Title: {self.__title}
Artist: {self.__artist}
Album: {self.__album}
Duration: {self.__duration}
'''
    def __repr__(self) -> str:
        return self.__title

# t1 = Duration(hour=0, minute=30, sec=20)
# t2 = Duration(minute=45, sec= 50)
# t3 = Duration(minute=3, sec= 45)
# t1.addDuration(t2)
# t1.addDuration(t3)
# # # # t1.addMinute(t3.getMinute())
# print(t1)