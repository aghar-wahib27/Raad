from .PhysicsEntities import physicsEntity, pygame

def movement():
    def jump(ent:physicsEntity):
        if not ent.reaction['down']:
            ent.jump['timer']+=1

        if ent.reaction['down'] and ent.jump['timer']:
            ent.jump['timer']=0
            ent.actions['jump_cond']=0

        if ent.actions['jump_cond']:
            ent.speed['y']=ent.jump['speed']

        if ent.jump['timer']>ent.jump['dur']:
            ent.speed['y']=-ent.jump['speed']

        print(ent.reaction,ent.movements)

    def supported(ent:physicsEntity):
        for key in ent.reaction.keys():
            if ent.reaction[key]:
                ent.reaction[key]=0

    def moment(ent:physicsEntity):
        if ent.actions['moment_x']:
            ent.speed['x'] *= ent.moment['x'] 
            ent.actions['moment_x'] = 0

        if ent.actions['moment_y']:
            ent.speed['y'] *= ent.moment['y'] 
            ent.actions['moment_y'] = 0


    def periodic(ent:physicsEntity):
        if ent.actions['reverse_x']:
            ent.speed['x'] *= -1
            ent.actions['reverse_x'] = 0

        if ent.actions['reverse_y']:
            ent.speed['y'] *= -1
            ent.actions['reverse_y'] = 0

    def parallize():
        ...
    def followx():
        ...
    def followy():
        ...
    def follow():
        ...

    return {'periodic':periodic,'parallize':parallize,
            'follow':follow,'followy':followy,'supported':supported,
            'followx':followx,'jump':jump,'moment':moment}

Movements = movement()

class Actors:
    def neighbors():
        ...

    def closest():
        ...

    def supporter():
        ...

    def sticker():
        ...

    Initializer = {}

class Acted:
    """
    if a PhysicsEntity uses this factory it MUST be a concius entity
    """
    def base(
                rect:pygame.rect,
                rules:list,
                movement:list,
            ):
        return physicsEntity(rect,rules,movement)

    def setActionDict(ent:physicsEntity,actions:dict={}):
        if hasattr(ent,"actions") :
            for key,value in actions.items():
                ent.actions[key] = value
        else:
            ent.actions=actions

    def jumper(
                ent:physicsEntity,
                jump_dur:int,
                jump_speed:int,
                jump_cond:bool,
                jump_cancel:bool
                ):
        ent.jump={'dur':jump_dur,'speed':jump_speed,'timer':0}
        Acted.setActionDict(ent,actions={'cancel_jump':jump_cancel,'jump_cond':jump_cond})
        ent.movements = { **{'jump': Movements['jump'] }, **ent.movements }

        return ent

    def supported(
            ent:physicsEntity
            ):
        ent.reaction={k:0 for k in ['up','down','right','left']}
        ent.movements['supported'] = Movements['supported']
        return ent

    def follower(
            ent:physicsEntity
            ):
        return ent

    def momented(
            ent:physicsEntity,
            momentx:int=1,
            momenty:int=1
            ):
        ent.moment={'x':momentx,'y':momenty}
        Acted.setActionDict(ent,{'moment_y':0,'moment_x':0})
        ent.movements['moment']=Movements['moment']
        return ent
        

    def bouncer(
            ent:physicsEntity,
            moment:int=1
            ):
        Acted.setActionDict(ent,{'reverse_y':0,'reverse_x':0,'reverse':0})
        ent.movements['periodic']=Movements['periodic']
        return Acted.momented(ent,moment,moment)

    Initializer = {'jump':jumper,'follow':follower,'supported':supported,
                   'bouncer':bouncer}

# PhysicsInitializer={'acted':Acted,'actor':Actors}
actedInit = Acted.Initializer
actorInit = Actors.Initializer
