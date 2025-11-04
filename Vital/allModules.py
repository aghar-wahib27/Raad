import json
import os
import pygame
from csv import reader
from abc import ABC,abstractmethod
from random import randint,choice
from copy import copy

pygame.init()
dims=(800,700)
scr=pygame.display.set_mode(dims)
clock = pygame.time.Clock() 

