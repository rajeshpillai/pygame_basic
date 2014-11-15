import pygame, sys
from classes import *
from process import process

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 360

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0,SCREENHEIGHT - 40,40,40,"images/bug.png")

while True:
	process(bug)
	bug.motion(SCREENWIDTH)

	screen.fill((0,0,0))
	BaseClass.allsprites.draw(screen)

	pygame.display.flip()

	clock.tick(FPS)