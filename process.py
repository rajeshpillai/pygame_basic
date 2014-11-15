import pygame, sys

def process(bug):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Returns a list of all the keys whther pressed or not
	keys = pygame.key.get_pressed()

	if keys[pygame.K_d]:
		bug.image = pygame.image.load("images/bug.png")
		bug.velx = 5
	elif keys[pygame.K_a]:
		bug.image = pygame.image.load("images/bugflipped.png")
		bug.velx = -5
	else:
		bug.velx = 0

