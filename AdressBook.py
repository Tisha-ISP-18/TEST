import pickle
 
class AdressBook:
 
    __data = {}
 
    def __init__(self, data:dict={})->None:
        self.__data = data
        return None
 
    def append(self, name:str, address:str)->bool:
        if name in self.__data:
            return False
        self.__data[name] = address
        return True
 
    def remove(self, name:str)->bool:
        if not name in self.__data:
            return False
        self.__data.pop(name)
        return True
 
    def items(self)->dict:
        return self.__data
 
    def change(self, name:str, address:str)->bool:
        if not name in self.__data:
            return False
        self.__data[name] = address
        return True
 
    def find(self, name:str)->str:
        if not name in self.__data:
            return 'Не существует'
        return self.__data[name]
 
    def save(self, path2file:str)->bool:
        with open(path2file, 'wb') as file:
            pickle.dump(self.__data, file)
        return True
 
    def load(self, path2file:str)->bool:
        with open(path2file, 'rb') as file:
            self.__data = pickle.load(file)
        return True