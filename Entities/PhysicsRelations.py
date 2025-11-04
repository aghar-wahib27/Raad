"""
write all your possible reltions here 
"""
from Vital.allModules import abstractmethod
from Vital.MathFunctions import closestDistanceBetweenPoints
from .PhysicsEntities import Relation,SYSTEMS
from math import ceil,floor

def checkImapct():
    def checkFromLittleAmount():
        ...
    
    def checkNeighbors():
        ...

    return {'little':checkFromLittleAmount,'neighbor':checkNeighbors}

Relations = {}

class Rule:
    @abstractmethod
    def rule(acted,actor):
        ...

    def check(acted,possible_actors):
        collied_tiles=[]
        for tile_rect in possible_actors:
            if tile_rect != acted : 
                if acted.rect.colliderect(tile_rect) :
                    collied_tiles.append(tile_rect)

        
        return collied_tiles 

class Support(Rule):
    name = 'support'

    def rule(acted,actors):
        colliding_in_y = Support.check(acted,actors)
        for tile_y in colliding_in_y:
            if acted.speed['x']<0:
                get_from = acted.rect.right-10
            if acted.speed['x']>0:
                get_from = acted.rect.left+10
            if acted.speed['x']:
                in_between = abs(get_from-tile_y.rect.center[0]) < floor(acted.rect.width/2 + tile_y.rect.width/2 )
            else:
                in_between=1
            
            if acted.speed['y']>0 and in_between :
                acted.reaction['down']=1
                acted.rect.bottom+=-acted.speed['y']
                acted.speed['y'] = min(0,acted.speed['y'])

            if acted.speed['y']<0  and in_between:
                acted.reaction['up']=1
                acted.rect.top+=-acted.speed['y']
                acted.speed['y'] = max(0,acted.speed['y'])

        colliding_in_x = Support.check(acted,actors)
        for tile in colliding_in_x:
            if acted.speed['x']>0 :
                acted.rect.right+=-acted.speed['x']
                acted.reaction['right']=1
                acted.speed['x'] = min(0,acted.speed['x'])
            if acted.speed['x']<0 :
                acted.reaction['left']=1
                acted.rect.left+=-acted.speed['x']
                acted.speed['x'] = max(0,acted.speed['x'])

    Relations[name] = {'rule' :rule,'check':Rule.check }

class GravititionalField(Rule):
    name='gravity'
    def returnG():
        return 9.81

    def field(mass1:int=0,mass2:int=0,radius:int=10):
        return ( GravititionalField.returnG() * mass1 * mass2 )/radius

    def rule(acted,actor):
        return 'hello from GravititionalField' , GravititionalField.field(15,14)

    def check(acted,possible_actors):
        ...

    Relations[name] = {'rule' :rule,'check':check }

class Stick(Rule):
    name = 'stick'
    def rule(acted,actor):
        ...
    def check(acted,possible_actors):
        ...

    Relations[name] = {'rule' :rule,'check':check }

class Bounce(Rule):
    name = 'bounce'

    def rule(acted,actors):
        if acted.speed['x']<0:
            get_from_x = acted.rect.left
        if acted.speed['x']>0:
            get_from_x = acted.rect.right
        if acted.speed['y']<0:
            get_from_y = acted.rect.top
        if acted.speed['y']>0:
            get_from_y = acted.rect.bottom

        for actor in actors:
            if acted.speed['x']:
                in_between_x = abs( abs(acted.rect.centerx - actor.rect.center[0] ) - (acted.rect.width/2 + actor.rect.width/2 )  ) <= abs(acted.speed['x']) + abs(actor.speed['x'])
                # if acted.speed['x']*actor.speed['x']<0:
                #     diff_in_speed= acted.speed['x']+actor.speed['x']
                # else:
                #     diff_in_speed = -( actor.speed['x'] )
                # in_between_x = abs( acted.rect.center[0]-actor.rect.center[0] ) + diff_in_speed< acted.rect.width/2 + actor.rect.width/2 
            else:
                in_between_x=1

            if acted.speed['y'] :
                # in_between_y = abs( acted.rect.center[1]- actor.rect.center[1]) - (acted.speed['y']+actor.speed['y']) < acted.rect.height/2 + actor.rect.height/2 
                in_between_y = abs( abs(acted.rect.centery-actor.rect.center[1] ) - (acted.rect.height/2 + actor.rect.height/2 )  ) <= abs(acted.speed['y']) + abs(actor.speed['y'])
            else:
                in_between_y=1

            if in_between_y:
                acted.actions['reverse_y']=1
                # actor.actions['reverse_y']=1
                acted.actions['moment_y']=1
                if acted.speed['y']>0:
                    acted.rect.bottom += -( acted.speed['y'] + actor.speed['y'] )
                else:
                    acted.rect.top += -( acted.speed['y'] + actor.speed['y'] )

            if in_between_x:
                acted.actions['reverse_x']=1
                # actor.actions['reverse_x']=1
                acted.actions['moment_x']=1
                if acted.speed['x']>0:
                    acted.rect.right += -( acted.speed['x'] + actor.speed['x'] )
                else:
                    acted.rect.left += -( acted.speed['x'] + actor.speed['x'] )


    Relations[name] = {'rule' :rule,'check':Rule.check }

def setAllRelations():
    for rel_name , rel_definers in Relations.items():
        SYSTEMS['physics'].setRelation(
                rel = rel_name.lower(),
                function = rel_definers['rule'],
                test = rel_definers['check']
                )

