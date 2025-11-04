from Vital import ABC,abstractmethod

class entity:
    def __init__(self,name,data):
        self.n = name
        self.data = data

    def get_data(self):
        return {'name':self.n}


SYSTEMS={}

class Sys(ABC):
    def __init__(self,name=''):
        self.entities = []
        if name : 
            SYSTEMS[name] = self

    @abstractmethod
    def Manage(self):
        ...
