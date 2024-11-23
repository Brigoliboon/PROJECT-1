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

        if temp >= 60:
            self.__minute = 0
            self.addMinute(temp)
        else:
            self.__minute = temp
        
    def addSecond(self, seconds:int):
        if seconds >= 60:
            self.addMinute(1)
            seconds -= 60
        temp = self.__second + seconds
        if temp >= 60:
            self.__second = 0
            self.addSecond(temp)
        else:
            self.__second = temp

    def addDuration(self, duration:'Duration')-> None:
        assert type(duration) is Duration, "Invalid duration"
        seconds = duration.durationSeconds()
        self.addSecond(seconds)

    def durationSeconds(self):
        total_sec = ((self.__hour*60)*60) + (self.__minute*60) + self.__second
        return total_sec

    def __str__(self) -> str:
        return "{:02}:{:02}".format(self.__minute, self.__second)