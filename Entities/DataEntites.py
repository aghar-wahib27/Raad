from Extractor import DATA_DICT,SEP
from Vital import load,save,searchObjByAttr,DirectedAttrSearch
from .System import Sys , entity

AllData={ k:load(v) for (k,v) in DATA_DICT.items() }


class DataSystem(Sys):
    def __init__(self):
        Sys.__init__(self,name='data')
        # self.lists={'all':[]}

    def ChangeEntities(self,Entities:list,Changes:list):
        ents = []
        for name in Entities :
            ents.append( searchObjByAttr(self.entities,['name',name])) 
        # print(ents,'this is the ents to be changed',Entities)
        for i in range(len(ents)):
            ents[i].ChangeData(Changes[i][0],Changes[i][1])

    def MapDataEntity(self,_name:str):
        for ent in self.entities:
            print(ent.get_data(),len(self.entities))
        return searchObjByAttr(self.entities,['name',_name])

    def Manage(self):
        for ent in self.entities:
            ent.save()


DT_SYS=DataSystem()


class DE(entity):
    """ DE : data entitiy
    """
    
    def __init__(self,_name:list,ap=1):
        # for n in self.n:
        # 	self.data=AllData[_name]
        # self.n=_name
        # self.data=AllData[_name]
        entity.__init__(self,name=_name,data=AllData[_name])
        if ap :
            DT_SYS.entities.append(self)


    def modify_data(self,gr:str,__type:any,mod:any):
        if __type==int:
            self.data[gr]+=mod

        if __type==list:
            self.data[gr].extend(mod)

        if __type==dict:
            for ke in mod.keys():
                self.data[gr][ke]=mod[ke]

    def ChangeData(self,_attr,new_val):
         # GetAttrFromNestedObj(self.data,_attr,change=[1,new_val])
        DirectedAttrSearch(self.data,_attr,change=[1,new_val,1])
        self.save()
        # print(self.data)

    # def get_data(self):
    #     # print({'name':self.n})

    #     return {'name':self.n}

    def save(self):
        save(DATA_DICT[self.n],AllData[self.n])

def IntializeAllDataEntites():
    for name in AllData:
        DE(name)

IntializeAllDataEntites()


