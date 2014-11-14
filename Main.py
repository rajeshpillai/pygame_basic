import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

clock = pygame.time.Clock()
FPS = 24
fivesecondinterval = FPS * 5
totalframes = 0

while True:
	#PROCESSES
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


#PROCESSES
#LOGIC

totalframes += 1

