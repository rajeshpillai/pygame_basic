import pygame, sys, classes, random

def process(bug, FPS, total_frames):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Returns a list of all the keys whther pressed or not
	keys = pygame.key.get_pressed()

	# Horizontal movement
	if keys[pygame.K_d]:
		bug.image = pygame.image.load("images/bug.png")
		bug.velx = 5
	elif keys[pygame.K_a]:
		bug.image = pygame.image.load("images/bugflipped.png")
		bug.velx = -5
	else:
		bug.velx = 0


	# Vertical movement
	if keys[pygame.K_w]:
		bug.jumping = True
		
	spawn(FPS, total_frames)

	
def spawn(FPS, total_frames):
	four_seconds = FPS * 4
	if total_frames % four_seconds == 0:
		r = random.randint(1, 2)
		# 50-50 chances of fly starting from either left or right
		x = 1
		if r == 2:
			x = 640 - 40


		fly = classes.Fly(x, 130, 40, 35, "images/fly.png")