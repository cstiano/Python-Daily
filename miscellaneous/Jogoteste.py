# importando modulos
import pygame, sys, os, time
from pygame.locals import *

#inicio dos modulos
pygame.init()
#window = pygame.display.set_mode((H,W))
#fim o programa pygame.display.quit() fechar tela
#titulo pygame.display.set_caption('titulo')
window = pygame.display.set_mode((800,600))

screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250,250,250))
screen.blit(background,(0,0))

File = os.path.join("Documentos","mario.png")
Image= pygame.image.load(File)
screen.blit(Image,(10,10))


#atualizar tela
pygame.display.flip()

pygame.display.set_caption('Teste')
time.sleep(2)
pygame.display.quit()