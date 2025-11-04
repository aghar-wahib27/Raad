from .allModules import reader

def importCsvLayout(path:str)->list:
    """
    ICL : import csv layout \n
    returns a list which upon it the level is built
    """
    with open(path) as level_map:
        overall_map=[]
        level = reader(level_map,delimiter=',')
        for row in level :
            overall_map.append(list(row))
        return overall_map

