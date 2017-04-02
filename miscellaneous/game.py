import pygame
import os, sys
from pygame.constants import*
tela = pygame.display.set_mode((300,200))
tela.fill((255,255,255))
rect1 = pygame.Surface((50,100))
rect1.fill((255,0,0))
tela.blit(rect1,(125,50))
pygame.display.update()