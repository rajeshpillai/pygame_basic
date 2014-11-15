import pygame, sys
from classes import *
from process import process

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 360

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
clock = pygame.time.Clock()
FPS = 24

background = pygame.image.load("images/forest.jpg")
bug = Bug(0,SCREENHEIGHT - 40,40,40,"images/bug.png")
fly = Fly(40, 100, 40,40,"images/fly.png")

while True:
	process(bug)
	bug.motion(SCREENWIDTH, SCREENHEIGHT)
	fly.fly(SCREENWIDTH)
	screen.blit(background, (0,0))
	BaseClass.allsprites.draw(screen)

	pygame.display.flip()

	clock.tick(FPS)