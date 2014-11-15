import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)
screen = pygame.display.set_mode((640,480))

# colors RGB()
clr1 = (22, 122, 211)
clr2 = (0, 44, 166)
clr3 = (34, 55, 245)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

while True:
	#PROCESSES
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	#PROCESSES
	#LOGIC
	screen.fill(white);
	pygame.draw.line(screen, clr2, (0 , 0), (640 , 360))
	pygame.display.flip()
