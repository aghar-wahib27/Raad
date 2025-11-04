import Extractor as ext
import Vital as vit
import Entities as ent



def getRandomRbgColor():
    return tuple( vit.randint(0,255) for _ in range(3) )

def isOverlap(p1,p2,diminsion):
    if abs( p1-p2 ) < diminsion:
        return True
    else : 
        return False

def getUnoverlapedPositions(size:int=5,diminsions:list[int]=[20,20]):
    previos_postions = [[vit.randint(80,300),vit.randint(80,300)]]
    while len(previos_postions)<size:
        next_positions = [vit.randint(80,300),vit.randint(80,300)]
        while not isOverlap(next_positions[0],previos_postions[-1][0],diminsions[0]) and not isOverlap(next_positions[1],previos_postions[-1][1],diminsions[1]) :
            previos_postions.append( [vit.randint(80,300),vit.randint(80,300)] )

    return previos_postions

ent.setAllRelations()

bouces = []

positions = getUnoverlapedPositions(10,[20,20])
# print('positions generated')
for i in range(5):
    bouces.append(
  ent.actedInit['bouncer'](
                ent.physicsEntity(
                    rect=vit.pygame.Rect(positions[i][0],positions[i][1],40,40),
                    roles=[
                           ['bounce','actor'],
                           ['bounce','acted'],
                           ]
                ),
                moment=1
                )
                )

for b in bouces:
    b.speed={'x':vit.randint(-7,7),'y':vit.randint(-7,7)}
    # b.speed={'x':7,'y':7}

expirement = vit.getGroupedRectList(  vit.importCsvLayout(  ext.CP(['Assets','levels_csv','exp.csv']) )  , rect_put_value = 0 , size =[20,20])
colors = []

for rec in expirement :
    ent.physicsEntity(
            rect=rec,
            roles=[ [ 'bounce', 'actor' ],[ 'support', 'actor' ]])

for _ in range(50):
    colors.append(getRandomRbgColor())



while 1 :
    vit.scr.fill('black')
    for i,rct in enumerate( expirement ) :
        vit.pygame.draw.rect(vit.scr,colors[i],rct)
    for i,b in enumerate(bouces):
        vit.pygame.draw.rect(vit.scr,colors[-i],b.rect)
        # print(b.actions)
        b.movement()
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

            if event.key in [vit.pygame.K_UP,vit.pygame.K_DOWN]:
                ent.Handler.update_event('up',val=0)
                ent.Handler.update_event('down',val=0)

    vit.clock.tick(10)
    vit.pygame.display.update()

vit.pygame.quit()

