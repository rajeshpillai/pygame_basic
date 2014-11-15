import pygame, sys
from classes import *
from process import process

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 360

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
clock = pygame.time.Clock()
FPS = 24
total_frames = 0

background = pygame.image.load("images/forest.jpg")
bug = Bug(0,SCREENHEIGHT - 40,40,40,"images/bug.png")
fly = Fly(40, 100, 40,40,"images/fly.png")
fly1 = Fly(40, 200, 40,40,"images/fly.png")
fly2 = Fly(40, 300, 40,40,"images/fly.png")
fly3 = Fly(40, 400, 40,40,"images/fly.png")


while True:
	process(bug, FPS, total_frames)
	bug.motion(SCREENWIDTH, SCREENHEIGHT)
	Fly.movement(SCREENWIDTH)
	BugProjectile.movement()
	total_frames += 1
	
	screen.blit(background, (0,0))
	BaseClass.allsprites.draw(screen)

	pygame.display.flip()

	clock.tick(FPS)