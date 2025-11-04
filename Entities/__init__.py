from .AnimationEntites import *
from .PhysicsEntities import *
from .DataEntites import *
from .PhysicsRelations import setAllRelations
from .PhysicsEntitiesFactories import actedInit,actorInit
from .AiEntites import concius,AiSystem
from .EventEntites import Handler,EE
from .System import SYSTEMS



class container:
    def __init__(self):
        self.entities=[]
        self.inter={}
    
    def clear(self):
        self.entities.clear()



    
