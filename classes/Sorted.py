#Name: Irfan Nasim
#Admission Number: 2201816
#Class: DAAA/FT/2B/07
import bisect

class DataItem:
    def __init__(self, file_name, caesar_key, text_length):
        self.__file_name = file_name
        self.__caesar_key = caesar_key
        self.__text_length = text_length

    @property
    def file_name(self):
        return self.__file_name

    @property
    def caesar_key(self):
        return self.__caesar_key

    @property
    def text_length(self):
        return self.__text_length

    def __lt__(self, other):
        return (self.__caesar_key, self.__text_length) < (other.__caesar_key, other.__text_length)

class SortedList:
    def __init__(self):
        self.__data = []

    @property
    def data(self):
        return self.__data

    def push(self, file_name, caesar_key, text_length):
        # Use bisect to find the insertion index
        new_item = DataItem(file_name, caesar_key, text_length)
        index = bisect.bisect_left(self.__data, new_item)
        
        # Insert the new tuple at the calculated index
        self.__data.insert(index, new_item)

    def clear(self):
        self.__data = []