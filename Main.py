import pygame, sys

pygame.init()

WIDTH, HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
img_bug = pygame.image.load("bug.png")

while True:
	#PROCESSES
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	screen.blit(img_bug, (200,200))
	pygame.display.flip()
