
def updateDictionary(inp:dict,v:str,state:list=[0,1,0]):
    """UD: update dictionary
    
    either add an item or remove it depends on the state arg
    

    Args:
        inp (dict): dictionary to be updated
        v (str): key to be added or removed 
        state (list, optional): first two values detrimine wether to add or remove from the original dict,
        the third is the item to be added if the state is adding

    Returns:
        dict: the updated dictionary 
    """
    dic={}
    lofk=list(inp.keys())
    if state[1]:
        lofk.remove(v)
    if state[0]:
        dic[v]=state[2]
        
    for i in lofk:
        dic[i]=inp[i]
    print(f'the old dict: {inp}, the updated one is :{dic}')
    return dic


def sortDictionaries(li:list,order_string='o'):
    """
    GOL : get orderd list (from list of dictionaries)

    a bad error has been found that is if two dict of the mother list happen to have the same order the function get suck in an infinite loop 
    althuogh in this project the function isnt required to handle this situation it should be fixed 
    """
    lin=[]
    oli=sorted([i[order_string] for i in li ])
    # for i in li:
    #     lin.insert(i['o'],i)

    while len(lin) != len(li):
        for o in oli:
            for ii in li :
                if ii[order_string]==o:
                    lin.append(ii)
    return lin


def getChildDictionary(d:dict,group_name:list)->any:
    """
    GCD : get child dict
    Args:
        d (dict): parent dict
        group_name (list): keys to search the child dict
    """
    
    di=d
    i=1
    de=group_name[0]
    while i :
            
            if type(di[de])==dict:
                i+=1
                di=di[de]
                de=group_name[i-1]
                print('lol')
               
            else:
                i=0
       
    return di[de]  

def searchObjByAttr(obj_li:list,req_data:list):
    for obj in obj_li : 
        data=obj.get_data()
        if data[req_data[0]]==req_data[1]:
            return obj

    return 'not_found'

def combineDictionaries(*args):
    """
    combine dictionaries from list of dictionaries
    """
    main = {} 
    for dic in args:
        main |= dic
    return main

def TurnListIntoDict(__lis:list,change=0):
    if change:
        co = __lis
    else:
        co = deepcopy(__lis)
    return { str(k):co[k] for k in range(len(co)) }

def GetAttrFromNestedObj(obj:dict,attr:str,change=[0,0,0]):
    """
    write discription here 
    this function has two jobs searching a nested dictionary and changeing a value in it which is a bas design
    """
    search = 1 
    if change[0]:
        co = obj
    else:
        co = copy.deepcopy(obj)

    next_level_objs = [co]
    value = 0
    while search: 
        co = next_level_objs[0]
        next_level_objs.pop(0)
        for k in co.keys():

            if k == attr:
                if change[0]:
                    if change[1]!=None:
                        co[k]=change[1]
                value = co[k]
                search = 0

            if type(co[k])==dict:
                next_level_objs.append(co[k])
    if type(value) == list :
        value = TurnListIntoDict(value,change=1)
    return value 

def DirectedAttrSearch(obj,attrs:str,change=[0,0,1]):
    attrsList = [attrs] if '+' not in attrs else attrs.split('+')
    print(attrsList)
    if change[2]:
        objCopy = obj
    else:
        objCopy = deepcopy(obj)
    for attr in attrsList:
        ch = [1,None,1] if attrsList.index(attr)!=len(attrsList)-1 else change
        # print(ch)
        objCopy = GetAttrFromNestedObj(objCopy,attr,change=ch)
        # print(objCopy)
    return objCopy

def flatten(lis:list):
    """
    combine nested lists into one big list
    """
    lu=[]
    h=copy(lis)
    for i in h:
        if type(i)!= list:
            lu.append(i)
        else:
            lu.extend(flatten(i))
            
    return lu

def NodeFlatten(lis:list):
    """
    flatten the node herarichy provided the root node only print
    """
    h=[copy(lis)]
    reached_bottom=0
    while not reached_bottom:
        lu=[]
        for n in h[-1]:
            lu.append(n.children)
        h.append( REFL(flatten(lu),[None]))
        if 'node' in [i.t for i in h[-1]]:
            reached_bottom=0
        else:
            reached_bottom=1

    return flatten(h)

def SN(parent:any,name:str):
    """
    search node
    """
    nodes=copy(parent.children)
    nodes.append(parent)
    s=1

    while s:
        search=ROUA(nodes,['nodename',name])
        # print('nodes ate',[i.nodename for i in nodes])
        if type(search) !=str:
            return search
        else:
            nodes= flatten([n.children for n in nodes if n.t!='leaf'])


