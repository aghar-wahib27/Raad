import sys
import os
sys.path.append(os.getcwd())

import Extractor as ext
import Vital as vit
import Entities as ent



def getRandomRbgColor():
    return tuple( vit.randint(0,255) for _ in range(3) )

ent.setAllRelations()

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


        if event.type==vit.pygame.KEYUP:
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

    if p1.listener.events['up']:
                p1.speed['y']=-10
        
    if p1.listener.events['down']:
                p1.speed['y']=10
    # print(p1.rect.x,p1.rect.y,p1.speed)
    vit.clock.tick(10)
    vit.pygame.display.update()

vit.pygame.quit()

