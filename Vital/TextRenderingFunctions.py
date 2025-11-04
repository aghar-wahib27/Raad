
def findWordFromText(w:str='@',text:list=[])->int:
    """FWFT : find word from text

    Args:
        w (str, optional): word to search for i the given text. Defaults to '@'.
        text (list, optional): list of words to search the word. Defaults to [].

    """ 
    #print(text)
    if w in text:
        #print('fint it')   
        return 1
    else:
  
        return 0

def extractTextUponLength(text:str,lw:int=12,font_size:int=0)->tuple:
    """EDUL : extract dialouge upon legth 
    
    extract dialouge of an npc upon one long sentence
    
    it can be used to divide any text `text` to sentences with equal no of words   `lw`
    
    then turns them to pygame surface and append to a list to be returned with its length
    """
    
    ess:dict={'counter':[0,0],'words_to_ignore':['9','#'],"status":'',"list_of_sec":[],"a_list_of_sec":[],
                        'list_of_sur':[],"new_sen":[],'list_of_words':text.split()}
    
    for single in ess['list_of_words']:

        ess["counter"][0]+=1
        ess["counter"][1]+=1
        
        if ess['status']=='break':
            ess['status']=''
        if single=='9':
            ess['status']='break'  
            ess["counter"][0]=1
        
        if ess["counter"][0]%lw!=0  and ess['status']=='':
            if  not ess['words_to_ignore'].count(single) :
                ess['new_sen'].append(single)
        else:
            if ess['status']=='break' or ess["counter"][0]%lw==0 :  #casses where I break the line and add a new sentence
                if  not ess['words_to_ignore'].count(single) :
                    ess['new_sen'].append(single)
                               
            ess['list_of_sec'].append(ess['new_sen'])
            ess['new_sen']=[]
           
        
    if len(ess['list_of_words'])%lw!=0:
            nl=REFL(ess['list_of_words'],['9','@'])
            ng=IOT(nl,ess['list_of_sec'][-1][-1])[-1]+1
        
            ess['list_of_sec'].append(REFL(nl[ng:],['#']))
    
    ess['a_list_of_sec']=ess['list_of_sec'].copy()
    ess['list_of_sec']=REFL(ess['list_of_sec'],['@'])
    
    for list in ess['list_of_sec']:
            ess['list_of_sur'].append(_FONTS_[font_size+2].render(" ".join(list),True,(255,255,255)))

    return ess['list_of_sur'] , len(ess['list_of_sec']) ,ess['a_list_of_sec']     

def widthOfWord(word:str,font_size:int):
    return (len(word)+1)*font_size

def extractTextUponLength2(text:str,lw:int=12,font_size:int=0)->tuple:
    """EDUL : extract dialouge upon legth 
    
    extract dialouge of an npc upon one long sentence
    
    it can be used to divide any text `text` to sentences with equal no of words   `lw`
    
    then turns them to pygame surface and append to a list to be returned with its length
    """
    
    ess:dict={'counter':[0,0],'words_to_ignore':['9','#'],"status":'',"list_of_sec":[],"a_list_of_sec":[],
                        'list_of_sur':[],"new_sen":[],'list_of_words':text.split()}
    
    for single in ess['list_of_words']:

        ess["counter"][0]+=1
        ess["counter"][1]+=1
        
        if ess['status']=='break':
            ess['status']=''
        if single=='9':
            ess['status']='break'  
            ess["counter"][0]=1
        
        if ess["counter"][0]%lw!=0  and ess['status']=='':
            if  not ess['words_to_ignore'].count(single) :
                ess['new_sen'].append(single)
        else:
            if ess['status']=='break' or ess["counter"][0]%lw==0 :  #casses where I break the line and add a new sentence
                if  not ess['words_to_ignore'].count(single) :
                    ess['new_sen'].append(single)
                               
            ess['list_of_sec'].append(ess['new_sen'])
            ess['new_sen']=[]
           
        
    if len(ess['list_of_words'])%lw!=0:
            nl=REFL(ess['list_of_words'],['9','@'])
            ng=IOT(nl,ess['list_of_sec'][-1][-1])[-1]+1
        
            ess['list_of_sec'].append(REFL(nl[ng:],['#']))
    
    ess['a_list_of_sec']=ess['list_of_sec'].copy()
    ess['list_of_sec']=REFL(ess['list_of_sec'],['@'])
    
    # for list in ess['list_of_sec']:
    #         ess['list_of_sur'].append(_FONTS_[font_size+2].render(" ".join(list),True,(255,255,255)))

    return ess['list_of_sur'] , len(ess['list_of_sec']) ,ess['list_of_sec']     


def extractTextUponSize(text:str,allowed_width:int,Font:any)->list :
    """EDUS : extract dialouge upon size
    
      to be written
    """
    ess:dict={'acc_width':0,'words_to_ignore':['9','#'],"status":'',"list_of_sec":[],"a_list_of_sec":[],
                        'list_of_sur':[],"new_sen":[],'list_of_words':text.split(),'fs':0,'gs':0,'gaps':0}

    ess['fs']=Font.render(ess['list_of_words'][0],1,(0,0,0)).get_width()//len(ess['list_of_words'][0])


    for single in ess['list_of_words']:


        if sum([WOW(wr,ess['fs']) for wr in ess['new_sen']+[single] ]) > allowed_width or single =='9' :
            ess['status']='break'
 
        if single not in ess['words_to_ignore']:
            ess['acc_width']+=WOW(single,ess['fs'])

       


        if ess['status']=='break':
            ess['status']=''
            ess['acc_width']=0

        if ess['acc_width']==0:
        
            # if single not in ess['words_to_ignore'] :
            #         ess['new_sen'].append(single)
                               
            ess['list_of_sec'].append(ess['new_sen'])
            ess['new_sen']=[]


        if ess['status']=='':
                print(ess['acc_width'],ess['fs'],single)

                if single not in ess['words_to_ignore'] :
                    ess['new_sen'].append(single)

    if len(ess['new_sen']):
            ess['list_of_sec'].append(ess['new_sen'])



    for lis in ess['list_of_sec']:
            ess['list_of_sur'].append(Font.render(" ".join(lis),True,(255,255,255)))

    return [ess['list_of_sur'] , len(ess['list_of_sec']),ess['fs'] ,ess['list_of_sec'] ]

