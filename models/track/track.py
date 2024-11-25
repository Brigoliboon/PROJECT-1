from duration import Duration
class Track:
    def __init__(self, title:str, artist:str,album:str, duration:Duration) -> None:
        self.__trackID = 0
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__duration:Duration = duration

    def getTrackID(self):
        return self.__trackID

    def getTitle(self):
        return self.__title
    
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def getDuration(self):
        return self.__duration
    
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