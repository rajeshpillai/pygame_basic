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

i = 0
while True:
	#PROCESSES
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	#PROCESSES
	#LOGIC
	i += 5
	if i > 255:
		i %= 255


	screen.fill((i,i,i))

	pygame.draw.line(screen, clr2, (0 , 0), (640 , 360))
	pygame.draw.rect(screen, clr3, (40,40,300,45))
	pygame.draw.circle(screen, clr1, (350,200), 80, 40)
	pygame.display.flip()
