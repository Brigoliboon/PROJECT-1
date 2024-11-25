class Pagination:
    """
    A class to handle pagination of a list of items.

    Attributes:
        arraySize (int): The total number of items in the array.
        itemCount (int): The number of items to display per page.
        page_count (int): The current page number.
        page_limit (int): The total number of pages available.
    """
    def __init__(self, arraySize:int, itemCount:int = 10):
        """
        Initializes the Pagination object with the total array size and item count.

        Args:
            arraySize (int): The total number of items in the array.
            itemCount (int, optional): The number of items to display per page. Defaults to 10.
        """
        self.arraySize = arraySize
        self.itemCount = itemCount
        self.page_count = 1
        self.__setPaginationLimit()

    def setArraySize(self, value:int)-> None:
        """
        Sets the total number of items in the array and updates pagination limits.

        Args:
            value (int): The new total number of items in the array.

        Raises:
            AssertionError: If the value is negative.
        """
        assert value >=0, "Invalid value range"
        self.arraySize = value
        self.__setPaginationLimit()

    def getStartIndex(self):
        """
        Calculates the starting index for the current page.

        Returns:
            int: The starting index of the current page.
        """
        index = (self.page_count - 1) * self.itemCount
        return index

    def getEndIndex(self):
        """
        Calculates the ending index for the current page.

        Returns:
            int: The ending index of the current page.
        """
        index = self.page_count * self.itemCount
        if self.page_count == self.page_limit:
            index -= (index-self.arraySize)
        return index

    def next(self):
        """
        Advances to the next page if it is not the last page.
        """
        if self.page_count < self.page_limit:
            self.page_count += 1

    def previous(self):
        """
        Goes back to the previous page if it is not the first page.
        """
        if self.page_count > 1:
            self.page_count -= 1

    def __setPaginationLimit(self)-> None:
        """
        Sets the pagination limits based on the total number of items and items per page.
        """
        quotient = self.arraySize//self.itemCount
        self.page_limit = 1 if int(quotient) < 1 else int(quotient)
        if type(quotient) is float:
            self.page_limit += 1
    
    def __str__(self) -> str:
        """
        Returns a string representation of the current pagination status.

        Returns:
            str: A string indicating the current page and total pages.
        """
        return f"<Page {self.page_count} of {self.page_limit}>"