from manager import *
from Vital import pygame,scr,GAME_STATE
import Entities as ent

clock=pygame.time.Clock() 

while GAME_STATE['run']:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:        
            GAME_STATE['run']=0

        if event.type==pygame.KEYDOWN:
            ent.Handler.update_event(event='key_down')
            if event.key == pygame.K_ESCAPE:
                ent.Handler.update_event(event='esc')


            if event.key == pygame.K_SPACE:
                ent.Handler.update_event(event='space')

        if event.type==pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            ent.Handler.update_event(event='mouse_down')

        if event.type==pygame.MOUSEBUTTONUP:
            ent.Handler.update_event(event='mouse_released')


    if len(ent.Handler.events['mouse_pos']):
        ent.Handler.update_event(event='mouse_pos',val=pygame.mouse.get_pos())
    
    running()
    ent.ANIM_SYS.Manage()
    clock.tick(18)
    # print(len(ent.ANIM_SYS.lists['ents']))

    pygame.display.update()
    
pygame.quit()
