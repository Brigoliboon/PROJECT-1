class Pagination:
    def __init__(self, arraySize:int, itemCount:int = 10):
        self.arraySize = arraySize
        self.itemCount = itemCount
        self.page_count = 1
        self.__setPaginationLimit()

    def setArraySize(self, value:int)-> None:
        assert value >=0, "Invalid value range"
        self.arraySize = value
        self.__setPaginationLimit()

    def getStartIndex(self):
        index = (self.page_count - 1) * self.itemCount
        return index

    def getEndIndex(self):
        index = self.page_count * self.itemCount
        if self.page_count == self.page_limit:
            index -= (index-self.arraySize)
        return index

    def next(self):
        if self.page_count < self.page_limit:
            self.page_count += 1

    def previous(self):
        if self.page_count > 1:
            self.page_count -= 1

    def __setPaginationLimit(self)-> None:
        quotient = self.arraySize//self.itemCount
        self.page_limit = 1 if int(quotient) < 1 else int(quotient)
        if type(quotient) is float:
            self.page_limit += 1
    
    def __str__(self) -> str:
        return f"<Page {self.page_count} of {self.page_limit}>"