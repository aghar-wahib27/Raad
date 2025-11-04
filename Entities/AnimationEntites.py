from Vital import ABC,abstractmethod,pygame,scr,blurImage,GAL3,choice,GAME_STATE
from .System import Sys

class AimationSystem(Sys):
    """
    uses singleton pattern
    """
    def __init__(self):
        Sys.__init__(self,name='anim')
        self.lists={'ents':[],'rects':[]}
        self.bgs={"layers":{},"wallpapers":{}}
        self.layers={}

        self.FadeScreen = 0 

    def draw_rect(self):
        for rct in self.lists['rects']:
            pygame.draw.rect(scr,rct.color,rct.rect)
        
    def StartFade(self,changes=[0,0],fadePeriod=20,**kargs):
        GAME_STATE['fade'][0]=1
        GAME_STATE['fade'][1]=fadePeriod
        GAME_STATE['fade'][-1]=1
        if changes[0]:
            GAME_STATE['change'][0]=1
            GAME_STATE['UI']=kargs['new_ui']

        if changes[1]:
            GAME_STATE['change'][1]=1
            GAME_STATE['level']=kargs['new_level']
    
    def BgFade(self):
        if GAME_STATE['fade'][0] == 1 :
            self.FadeScreen.style['fade'][1]=10
            self.FadeScreen.style['fade'][0]=10
            GAME_STATE['fade'][0]=0

        if self.FadeScreen.style['fade'][0] >=255 and GAME_STATE['fade'][1]:
            GAME_STATE['fade'][1] += -1
            if GAME_STATE['fade'][1]==15:
                GAME_STATE['fade'][-1]=0
            if GAME_STATE['fade'][1]==0:
                GAME_STATE['fade'][0]=2

        
        if GAME_STATE['fade'][0] == 2:
            self.FadeScreen.style['fade'][1] = -10
            self.FadeScreen.style['fade'][0]=255
            GAME_STATE['fade'][0]=0

        self.FadeScreen.AnimationPlayer()

    def Manage(self):
        """
        uses the facade pattern
        """

        for ent in self.entities:
            ent.AnimationPlayer()

        self.BgFade()

ANIM_SYS=AimationSystem()

def AnimationTypes()->list: 
    def put(oe:any):
        oe.display.blit(oe.img,oe.pos)
    
    def fade(oe:any):
        oe.img.set_alpha(oe.style['fade'][0])
        if 9< oe.style['fade'][0]<256:
            oe.style['fade'][0] += oe.style['fade'][1]
            print('fading in or out',oe.style['fade'])
        oe.display.blit(oe.img,oe.pos)

    def BackGroundPut(oe:any):
        oe.main_sur.blit(oe.img,oe.pos)
        for anim in oe.anims:
            anim.AnimationPlayer()
        oe.display.blit(blurImage(oe.main_sur,oe.blur),oe.pos)

    def AllAnimationsController(oe:any):
            """ACC : All Animations Controller 
            """
            if  0<oe.actions['allow_moveing']<3 :
                #self.anim['_n_'][3]='cd'
                if oe.anim["_n_"][0] in oe.anim["cha"]:
                    ne=oe.anim['_n_'][0] + oe.anim["_n_"][3]
                else:
                    ne=oe.anim['_n_'][0]
                
                oe.anim['_n_'][2]=ne
                oe.anim[oe.anim['_n_'][2]][1]=0
                oe.anim[oe.anim['_n_'][2]][0]=0
                oe.anim['_n_'][-1]=oe.anim['_n_'][-2]  

            if oe.anim[oe.anim['_n_'][2]][0] != oe.anim[oe.anim['_n_'][2]][2]:
                oe.anim[oe.anim['_n_'][2]][0]+=1
            else:
                oe.anim[oe.anim['_n_'][2]][0]=0
                oe.anim[oe.anim['_n_'][2]][1]+=1
            

            if oe.anim[oe.anim['_n_'][2]][1]  == len(oe.OBJ[oe.anim['_n_'][2]]) :
                
                # oe.anim[oe.anim['_n_'][2]][1]=0
                oe.anim[oe.anim['_n_'][2]][1]=0

                if oe.anim[oe.anim['_n_'][2]][-1]=='o':
                    oe.actions['allow_moveing']=1
                    oe.anim['_n_'][0]=oe.anim['_n_'][1] 
                
                   
                
            
            # print( oe.anim['_n_'][:3],oe.actions['allow_moveing'],oe.anim [ oe.anim['_n_'][2] ] )        
            if oe.anim[oe.anim['_n_'][2]][-1]=='o':
                    oe.actions['allow_moveing']=3
                    
            if oe.anim[oe.anim['_n_'][2]][-1]=='p':
                    oe.actions['allow_moveing']=0
                    #oe.AM()

            # print( oe.anim['_n_'][2] , oe.anim [ oe.anim['_n_'][2] ])
               
            if oe.anim['_n_'][-1]=='right':
                oe.display.blit(oe.OBJ[oe.anim['_n_'][2]][oe.anim [ oe.anim['_n_'][2] ] [1]],oe.pos)
            else:
                oe.d.blit(pygame.transform.flip(oe.OBJ[oe.anim['_n_'][2]][oe.anim [ oe.anim['_n_'][2] ] [1]],True,False),oe.pos)

    def BackGroundAnimtaion(oe:any):
        oe.anim[0]+=1

        if oe.anim[0]==oe.anim[2]:
            oe.anim[0]=0
            oe.anim[1]+=1

        if oe.anim[1]==len(oe.frames):
            oe.anim[1]=0
            oe.anim[2]=choice(oe.speeds)

        oe.display.blit(oe.frames[oe.anim[1]],oe.pos)

    return {'P':put,'BP':BackGroundPut,'ACC':AllAnimationsController,"BGA":BackGroundAnimtaion,'FD':fade}

AT=AnimationTypes()

class Animation:
    def __init__(self,ap=1,**kargs):
        if type(kargs['type']) == list :
            self.animationfunc = { k : AT[ k ] for k in kargs['type']}
        else:
            self.animationfunc=AT[kargs['type']]
        self.display=kargs['display']
        self.pos=kargs['position']

        if ap:
            ANIM_SYS.entities.append(self)

    def remove(self):
        if self in ANIM_SYS.lists['ents']: 
            ANIM_SYS.lists['ents'].remove(self)


    def AnimationPlayer(self):
        """
        similar to the adapter pattern
        """
        self.animationfunc(self)

class AnimationFactory:
    @staticmethod
    def AnimationObject(**kargs)->Animation:
        AO=Animation(ap=kargs['ap'],type=kargs['type'],display=kargs['display'],position=kargs['position'])
        AO.img=kargs['img']
        AO.style = {}
        if 'fade' in kargs:
            AO.style['fade'] = [5,0,10]
        if 'resize' in kargs:
            AO.img=pygame.transform.scale(AO.img,kargs['resize'])   
        return AO

    @staticmethod
    def AnimationEntity(**kargs)->Animation:
        AE=Animation(type='ACC',display=scr,position=kargs['position'])
        AE.anim:dict[str,list]={k:v for (k,v) in zip( [i for i in kargs['keys']] , [i for i in kargs['args']]) }
        AE.AA=kargs['all_animations']       
        return AE

    @staticmethod
    def BackGroundAnimation(**kargs)->Animation:
        BGA=Animation(ap=0,type='BGA',display=kargs['display'],position=kargs['position'])
        BGA.frames=GAL3(img=kargs['img'],no_of_frames=kargs['nf'],start=kargs['start'],w=kargs['w'],h=kargs['h'])
        BGA.speeds=kargs['fr_speed']
        BGA.anim=[0,0,choice(BGA.speeds)]
        BGA.layer=kargs['layer']

        return BGA

    @staticmethod
    def Background(**kargs)->Animation:
        BG=AnimationFactory.AnimationObject(ap=0,img=kargs['img'],type='BP',display=scr,position=(0,0),resize=scr.get_size())
        BG.main_sur=pygame.Surface(BG.img.get_size())
        # BG.display=BG.main_sur
        BG.main_sur.set_colorkey((0,0,0))
        BG.blur=kargs['blur']
        return BG


    @staticmethod
    def UiAnimation(**kargs)->Animation:
        uia=AnimationFactory.AnimationObject(type='BGA',display=scr,position=kargs['position'])
        return uia

    ANIMS={"AO":AnimationObject,"AE":AnimationEntity,"BGA":BackGroundAnimation,"BG":Background,"UIA":UiAnimation}

AnimF=AnimationFactory()

class Background:
    def __init__(self,**kargs):
        self.bgs={
            k:v for (k,v) in 
                zip(
                    [name for name in kargs['bg_names']],[img for img in kargs['bg_imgs'] ]
                    )
                }

        self.bg_anims=kargs['bg_ainmations']
        for anim in self.bg_anims:
            anim.display=self.bgs[anim.layer].main_sur

        for bg in self.bgs:
            self.bgs[bg].anims=[bg_anim for bg_anim in self.bg_anims if bg_anim.layer == bg ]


        self.bgs_list=[self.bgs[ord_name] for ord_name in sorted(self.bgs.keys(),key=lambda x:int(x[-1]))]
        ANIM_SYS.lists['ents'].extend(self.bgs_list)

