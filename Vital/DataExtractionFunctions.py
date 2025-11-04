
def load(path:str):
    with open(path,'r') as pth:
        data=json.load(pth)

    return data

def save(path:str,obj:any):
    with open( path,'w') as dta:
                json.dump(obj,dta,indent="\t")

