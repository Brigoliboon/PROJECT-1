class Duration:
    """
    A class to represent a duration of time in hours, minutes, and seconds.

    Attributes:
        __hour (int): The hour component of the duration.
        __minute (int): The minute component of the duration.
        __second (int): The second component of the duration.
    """
    def __init__(self, hour:int = 00, minute:int = 00, sec:int = 00) -> None:
        """
        Initializes the Duration object with hours, minutes, and seconds.

        Args:
            hour (int, optional): The hour component. Defaults to 0.
            minute (int, optional): The minute component. Defaults to 0.
            sec (int, optional): The second component. Defaults to 0.
        """
        self.__hour = hour
        self.__minute = minute
        self.__second = sec
    
    def getHour(self):
        """
        Returns the hour component of the duration.

        Returns:
            int: The hour component.
        """
        return self.__hour
    
    def getMinute(self):
        """
        Returns the minute component of the duration.

        Returns:
            int: The minute component.
        """
        return self.__minute
    
    def getSecond(self):
        """
        Returns the second component of the duration.

        Returns:
            int: The second component.
        """
        return self.__second
    
    def addHour(self, hour):
        """
        Adds the specified number of hours to the duration.

        Args:
            hour (int): The number of hours to add.
        """
        self.__hour += hour

    def addMinute(self, minute:int):
        """
        Adds the specified number of minutes to the duration.

        Args:
            minute (int): The number of minutes to add.
        """
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
        """
        Adds the specified number of seconds to the duration.

        Args:
            seconds (int): The number of seconds to add.
        """
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
        """
        Adds another Duration object to this duration.

        Args:
            duration (Duration): The Duration object to add.

        Raises:
            AssertionError: If the provided duration is not a Duration object.
        """
        assert type(duration) is Duration, "Invalid duration"
        seconds = duration.durationSeconds()
        self.addSecond(seconds)

    def durationSeconds(self):
        """
        Converts the duration to total seconds.

        Returns:
            int: The total duration in seconds.
        """
        total_sec = ((self.__hour*60)*60) + (self.__minute*60) + self.__second
        return total_sec

    def __str__(self) -> str:
        """
        Returns a string representation of the duration in the format "MM:SS".

        Returns:
            str: A formatted string representing the duration.
        """
        return "{:02}:{:02}".format(self.__minute, self.__second)