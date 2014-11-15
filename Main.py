import pygame, sys
from classes import *

pygame.init()

WIDTH, HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0,100,40,40,"images/bug.png")
bug2 = Bug(0,200,40,40,"images/bug.png")
bug3 = Bug(0,300,40,40,"images/bug.png")

while True:
	#PROCESSES
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	bug.motion()
	
	screen.fill((0,0,0))
	BaseClass.allsprites.draw(screen)

	pygame.display.flip()

	clock.tick(FPS)