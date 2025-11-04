from Vital.allModules import pygame
from .System import Sys , SYSTEMS


class Relation:
    def __init__(self,name:str=None,impact=None,check=None):
        self.__name = name
        self.entities = {'actor':[],'acted':[]}
        self.impact = impact
        self.check = check

    @property
    def name(self):
        return self.__name

    def ApplyImpact(self):
        for ent in self.entities['acted']:
            values = self.check(ent,self.entities['actor'])
            # print(self.name ,)

            # actors , isInField = self.check(ent,self.entities['actor'])
            if values :
                self.reaction(ent,values)

    def reaction(self,acted=None,actor=None):
        if acted and actor : 
            self.impact(acted,actor)
        else:
            raise ValueError('the actor and acted entities shouldnt be None , check your shouldApplyImpact method ')

    def __repr__(self):
        return f"<{self.name.upper()} relation with {len(self.entities['actor'])} actor and {len(self.entities['acted'])} acted upon>"

class PhysicsSystem(Sys):
    def __init__(self):
        Sys.__init__( self , name = 'physics')
        self.relations:dict[str:Relation] = {}

    def append(self,ent=None,roles=[]):
        if ent is None or len(roles)==0 :
            raise ValueError('improper args given to append in PhysicsSystem, roles should not be empty')
        else : 
            for role in roles :
                if role[1] in ['actor','acted'] :
                    if role[0] in self.relations:
                        self.relations[role[0]].entities[role[1]].append(ent)
                    else:
                        raise ValueError(f'{role[0]} is not a name of a relation, use setRelations to register it')
                else :
                    raise ValueError(f'physicsEntity should be an actor or acted not {role[1]}')


    def setRelation(self,rel,function,test):
            self.relations[rel] = Relation(name=rel,impact=function,check=test)
            

    def Manage(self):
        for relation in self.relations.values():
            relation.ApplyImpact()

class physicsEntity:
    def __init__(self ,
                 rect:pygame.rect = pygame.Rect(0,0,20,20),
                 roles:list[list] = [] ,
                 movement_type:list[str]=[]
                 ):
        SYSTEMS['physics'].append(ent=self,roles = roles)
        self.rect = rect 
        self.dirictions = {'r':0,'l':0,'d':0,'u':0}
        self.speed = {'x':0,'y':0}
        self.pos = {'x':0,'y':0}
        self.movements = {}
        if movement_type:
            for move in movement_type:
                if move in Movements:
                    self.movements[move] = Movements[move]
                else :
                    raise ValueError(f'the {move} type isnt provided, please provide a value which is in {self.Movements.keys()}')

    @property
    def is_moving_horizontally(self):
        return True if self.speed['x'] else False

    @property
    def is_moving_vertically(self):
        return True if self.speed['y'] else False

    @property
    def is_moving(self):
        return True if self.speed['y'] or self.speed['x'] else False

    def setMovementAtOrder():
        ...

    def movement(self):
        for movement_function in self.movements.values():
            movement_function(self)
        self.rect.x+=self.speed['x']
        self.rect.y+=self.speed['y']


PhysicsSystem()

