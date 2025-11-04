__doc__ = " refer to https://stackoverflow.com/questions/60593604/importerror-attempted-relative-import-with-no-known-parent-package if you ever faced that error , solved it from there "

import sys
import os
sys.path.append(os.getcwd())
print(sys.path)


import Extractor as ext
from Vital import pygame
fonts = {
        k.split('/')[-1].replace('.tff',''): ext.CP(['Assets','fonts',k]) 
        for k in 
        ext.LS_DIR(
                ext.CP(['Assets','fonts'])
            )
        }
def getRequiredFont(font:str='main_font',size:int=10):
    if font in fonts :
        return pygame.font.Font(font,int(k))
    else :
        raise ValueError(' specify a font from {available} '.format(
            available = list(fonts.keys())
            )
                         )

print(fonts)
main_font = ext.CP(['Assets','fonts','main_font.tff'])
# print(main_font)
FONT = pygame.font.Font(main_font,15) 
# __FONTS__={ k:pygame.font.Font(main_font,int(k)) for k in ['10','15','20','25','30','35','40','45','50','55','60','65'] }
