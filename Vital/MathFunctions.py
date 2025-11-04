from .allModules import pygame
import math

def closestDistanceBetweenRects(rect_1:pygame.Rect,rect_2:pygame.Rect,limits:list=[0,0])->bool:
    """
    checks the distance between two rectangles if its within the provided limits
    """
    if abs(rect_1.centerx-rect_2.centerx) < limits[0] and abs(rect_1.centery-rect_2.centery) < limits[1] :
        return True
    else:
        return False

def getColsestNumberFromMultiple(no:int,dv:int=3,st=[0,1])->int:
    """
    get the closest (least or biggest upon `st`  number from a multiple of `dv` defaulted to 3
    ex: 13->12, 20->18, 15->15 if `st[0]`
    ex: 13->15, 20->21, 15->15 if `st[1]`
    """
    cu=no%dv
    if no%dv == 0:
       return no
    else:
        if st[0]:
            return (no-cu)
        if st[1]:
            return (no-cu)+3

def closestDistanceBetweenPoints(p1:tuple,p2:tuple):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
