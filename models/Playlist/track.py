class Duration:
    def __init__(self, hour:int = 00, minute:int = 00, sec:int = 00) -> None:
        self.__hour = hour
        self.__minute = minute
        self.__second = sec
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def addHour(self, hour):
        self.__hour += hour

    def addMinute(self, minute:int):
        if minute >= 60:
            self.addHour(1)
            minute -= 60
        temp = self.__minute + minute

        if temp > 60:
            self.addMinute(temp)
        else:
            self.__minute = temp

    def addSecond(self, sec:int):
        if sec >= 60:
            self.addMinute(1)
            sec -= 60
        temp = self.__second + sec

        if temp > 60:
            self.addSecond(temp)
        else:
            self.__second = temp

    def addDuration(self, duration:'Duration')-> None:
        assert type(duration) is Duration, "Invalid duration"
        seconds = duration.durationSeconds()
        self.addSecond(seconds)

    def durationSeconds(self):
        total_sec = (self.__hour*60)*60 + self.__minute*60 + self.__second
        return total_sec

    def __str__(self) -> str:
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)


class Track:
    def __init__(self, title:str, artist:str,album:str, duration:int) -> None:
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__duration:Duration = duration
    
    def getTitle(self):
        return self.__title
    
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def getDuration(self):
        return self.__duration
    
    
    def __str__(self) -> str:
        return self.__title

    def __repr__(self) -> str:
        return self.__title
