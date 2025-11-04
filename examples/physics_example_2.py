import sys
import os
sys.path.append(os.getcwd())

import Extractor as ext
import Vital as vit
import Entities as ent



def getRandomRbgColor():
    return tuple( vit.randint(0,255) for _ in range(3) )

ent.setAllRelations()

p2 = ent.actedInit['jump'](
            ent.actedInit['supported'](
                ent.physicsEntity(
                    rect=vit.pygame.Rect(100,200,40,40),
                    roles=[
                           ['support','acted'],
                           ['support','actor'],
                           ['bounce','acted'],
                           [ 'stick','acted' ]
                           ]
                ))
            ,
            10,
            -10,
            0,
            0
        )
p1 = ent.actedInit['jump'](
            ent.actedInit['supported'](
                ent.physicsEntity(
                    rect=vit.pygame.Rect(200,100,40,40),
                    roles=[
                           ['support','acted'],
                           ['support','actor'],
                           ['bounce','acted'],
                           [ 'stick','acted' ]
                           ]
                ))
            ,
            10,
            -10,
            0,
            0
        )

p1.speed={'x':0,'y':0}
p1.listener = ent.EE(['right','left','up', 'down'])
p2.listener = ent.EE(['s','a','w', 'd'])

# print(ent.SYSTEMS['physics'].relations['support'].entities['acted'])
# for acted in ent.SYSTEMS['physics'].relations['support'].entities['acted']:
#     for actor in ent.SYSTEMS['physics'].relations['support'].entities['actor']:
#             print(acted,actor,acted==actor)

expirement = vit.getGroupedRectList(  vit.importCsvLayout(  ext.CP(['Assets','levels_csv','exp.csv']) )  , rect_put_value = 0 , size =[20,20])
colors = []

for rec in expirement :
    ent.physicsEntity(
            rect=rec,
            roles=[[ 'support', 'actor' ]])
    colors.append(getRandomRbgColor())



while 1 :
    vit.scr.fill('black')
    for i,rct in enumerate( expirement ) :
        vit.pygame.draw.rect(vit.scr,colors[i],rct)
    vit.pygame.draw.rect(vit.scr,(190,44,89),p1.rect)
    vit.pygame.draw.rect(vit.scr,(90,144,89),p2.rect)
    p2.movement()
    p1.movement()
    ent.SYSTEMS['physics'].Manage()
    for event in vit.pygame.event.get():
        if event.type==vit.pygame.KEYDOWN:
            if event.key == vit.pygame.K_RIGHT:
                ent.Handler.update_event('right')

            if event.key == vit.pygame.K_LEFT:
                ent.Handler.update_event('left')

            if event.key == vit.pygame.K_UP:
                ent.Handler.update_event('up')

            if event.key == vit.pygame.K_DOWN:
                ent.Handler.update_event('down')

            if event.key == vit.pygame.K_a:
                ent.Handler.update_event('a')

            if event.key == vit.pygame.K_d:
                ent.Handler.update_event('d')

            if event.key == vit.pygame.K_w:
                ent.Handler.update_event('w')

        if event.type==vit.pygame.KEYUP:
            ent.Handler.update_event('d',val=0)
            if event.key in [vit.pygame.K_a,vit.pygame.K_d]:
                ent.Handler.update_event('a',val=0)
                ent.Handler.update_event('w',val=0)
                p2.speed['x']=0
            if event.key in [vit.pygame.K_w]:
                ent.Handler.update_event('w',val=0)
                p1.speed['y']=0
            if event.key in [vit.pygame.K_RIGHT,vit.pygame.K_LEFT]:
                ent.Handler.update_event('right',val=0)
                ent.Handler.update_event('left',val=0)
                p1.speed['x']=0

            if event.key in [vit.pygame.K_UP,vit.pygame.K_DOWN]:
                ent.Handler.update_event('up',val=0)
                ent.Handler.update_event('down',val=0)
                p1.speed['y']=0

    if p1.listener.events['right']:
                p1.speed['x']=10

    if p1.listener.events['left']:
                p1.speed['x']=-10

    if p2.listener.events['a']:
                p2.speed['x']=10

    if p2.listener.events['d']:
                p2.speed['x']=-10

    if p2.listener.events['w']:
            p2.actions['jump_cond']=1
    if p1.listener.events['up']:
            p1.actions['jump_cond']=1
                # p1.speed['y']=-10
        
    # if p1.listener.events['down']:
    #             p1.speed['y']=10
    # print(p1.rect.x,p1.rect.y,p1.speed)
    vit.clock.tick(10)
    vit.pygame.display.update()

vit.pygame.quit()

