from Vital import pygame
import Extractor as ext



ui_assets = ext.CP_DIR( 
            ext.CP(['Assets','art','UIS'])
            )

print(ui_assets)

UIS={ ext.getFileNameFromPath(path) : pygame.image.load(path) for path in ui_assets }

for img in UIS.values():
	img.set_colorkey((0,0,0))

