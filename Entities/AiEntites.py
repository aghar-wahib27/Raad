from Vital import ABC,abstractmethod
from .System import Sys

class AiSystem(Sys):
    """
    uses singleton pattern
    """
    def __init__(self):
        # self.lists:dict[str,list]={"concius":[]}
        Sys.__init__(self,name='ai')

    def Manage(self):
        for ai_ent in self.entities:
            ai_ent.behavior()

AI_SYS=AiSystem()

class concius(ABC):
    def __init__(self,ap=1,**kargs):
        self.actions=kargs['actions']
        self.count:dict={}

        for ke in kargs['counters']:
            self.count[ke]=[0,0]
        if ap:
            AI_SYS.lists['concius'].append(self)

    def counts(self,**kargs):
            """
            COUNERNAME = [ CONDTION TO START COUNTING , TYPE OF COUNTING + DURATION , CONDTION TO STOP COUNTING]
            COUNERNAME : must be a counter name passed to the init count kargs , if it ends with 'o' it will be played once 
            TYPE OF COUNTING : un for looping ,o for counting once 
            """
            for k in kargs.keys():
              
                if kargs[k][0] and self.count[k][1]>=0:
                    self.count[k][1]=1

                if kargs[k][1].split('+')[0]=='un':
                    if self.count[k][0] == int(kargs[k][1].split('+')[1]) :
                        #self.count.pop(k)
                        if k[-1]=='o':
                            self.count[k][1]=-1
                        else:
                            self.count[k][1]=0
                        self.count[k][0]=0


                if kargs[k][2]:
                    if k[-1]=='o':
                        self.count[k][1]=-1
                    else:
                        self.count[k][1]=0
                        self.count[k][0]=0

                if self.count[k][1]>0:
                    self.count[k][0]+=1

    def inter(self,**kargs):
        for act in kargs.keys():
            for tpl in kargs[act]:
                if tpl[1]:
                    if self.actions[act]!=tpl[0]:
                        self.actions[act]=tpl[0]

    @abstractmethod
    def behavior(self):
        ...

