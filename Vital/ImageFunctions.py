from .allModules import pygame

def GI(image,frame,height_frame,height,width,color) -> pygame.Surface: 
    """GI : get image

    """
    if height>0 and width>0 :
        img=pygame.Surface((width,height)).convert_alpha()
        img.set_colorkey(color)
        img.blit(image,(0,0),(width*frame,height_frame,width,height))
        return img
    else:
        image.set_colorkey(color)    
        return image

def GAL(i,start,width,height,height_frame):
    """GAL : get animation list
    """
    list=[]
    for i in range(i):
        frame=GI(start+i,width,height,(0,0,0),height_frame).convert()
        list.append(frame)
    return list
 

def GAL2(img,i,start,width,height,height_frame):
        """GAL : get animation list
        """
        list=[]
        for i in range(i):
            #frame=GI(img,start+i,width,height,(0,0,0),height_frame).convert()
            frame=GI(img,start+i,height_frame*height,height,width,color=(0,0,0)).convert()
            list.append(frame)
        return list

def GI3(**kargs) -> pygame.Surface: 
        """GI : get image

        """
        #print(width,height)
        img=pygame.Surface((kargs['width'],kargs['height'])).convert_alpha()
        img.set_colorkey(kargs['color'])
        img.blit(kargs['img'],(0,0),(kargs['width']*kargs['start'][0],kargs['height']*kargs['start'][1],kargs['width'],kargs['height']))
        return img

def GAL3(**kargs):
        """GAL : get animation list
        """
        list=[]
        for i in range(kargs['no_of_frames']):
            frame=GI3(img=kargs['img'],start=[kargs['start'][0]+i,kargs['start'][1]],height=kargs['h'],width=kargs['w'],color=(0,0,0)).convert()
            list.append(frame)

        return list


def getAllSprites(anim_obj:dict,sprites_paths:list) -> dict:
    """GAS : get all sprites

    Args:
        anim_obj (dict): a dict of dict ,each one of the child dict contains a `_n_`  and an `anim` key for more info refer the `docm.txt` section `R:A`
        sprites_paths (list): list containing paths for png files 

    Returns:
        dict: dict of animations name and thier corspnding pygame surfaces
         
    """
     
    
    
    SPRITES={
    k:v for (k,v) in 
           zip(
               sorted([anim_obj[i]["_n_"] for i in anim_obj],key=lambda ce: ce[0:3]),
               [pygame.image.load(i) for i in sprites_paths]
               )
           }
    
    SURFACES={
    k:v for (k,v) in 
           zip(
               [anim_obj[i]["_n_"] for i in anim_obj],
               [ [GAL2(SPRITES[i[0]],i[1],0,i[3],i[4],k) for k in range(i[2])] for i in   [i for i in [ i['anim']['info'] for i in [i for i in anim_obj.values()]] ]  ]
               )
           }
    
    ANIM_DATA={k:v for (k,v) in zip([i for i in anim_obj],[anim_obj[i]['anim'] for i in anim_obj])}
    
    ANIM_INFO=[ (i,f,ANIM_DATA[i][f],SURFACES[i][ANIM_DATA[i][f][0]-1][ANIM_DATA[i][f][1]:ANIM_DATA[i][f][2]])  for i,j in ANIM_DATA.items() for f in j if f!='info'  ]
    
    ALL_ANIM={k:{i[1] : i[3] for i in ANIM_INFO if i[0]==k} for (k,_) in ANIM_DATA.items() }
    
    return ALL_ANIM
    
def risizeImage(img:pygame.Surface,new_size:tuple):
	return pygame.transform.scale(img,new_size)

def blurImage(img:pygame.Surface,factor:int):
	return pygame.transform.box_blur(img,factor)

