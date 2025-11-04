from .allModules import *
from .csvFunctions import *
from .DataExtractionFunctions import *
from .DictionaryManipulation import *
from .ImageFunctions import *
from .ListManipulation import *
from .MathFunctions import *
from .TextRenderingFunctions import *
from .LevelCreationFunctions import *

def singleton(cls):
    instacne={}
    def new(*args,**kargs):
        if cls not in instacne:
            instacne[cls]=cls(*args,**kargs)
        return instacne[cls]
    return new


GAME_STATE={
    "run":1,
    "UI":'',
    "level":"",
    "change":[0,0],
    "fade":[0,0,0]
    }


