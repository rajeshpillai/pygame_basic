import pygame, sys, classes, random

def process(bug, FPS, total_frames):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_e:
				classes.BugProjectile.fire = not classes.BugProjectile.fire

	# Returns a list of all the keys whther pressed or not
	keys = pygame.key.get_pressed()

	# Horizontal movement
	if keys[pygame.K_d]:
		classes.Bug.going_right = True
		bug.image = pygame.image.load("images/bug.png")
		bug.velx = 5
	elif keys[pygame.K_a]:
		classes.Bug.going_right = False
		bug.image = pygame.image.load("images/bugflipped.png")
		bug.velx = -5
	else:
		bug.velx = 0


	# Vertical movement
	if keys[pygame.K_w]:
		bug.jumping = True

	if keys[pygame.K_SPACE]:
		def direction():
			if classes.Bug.going_right:
				p.velx = 8
			else:
				p.image = pygame.transform.flip(p.image, True, False) # flip horizontally
				p.velx = -8

		if (classes.BugProjectile.fire):
			p = classes.BugProjectile(bug.rect.x, bug.rect.y,"images/projectiles/fire.png")
			direction()
		else:
			p = classes.BugProjectile(bug.rect.x, bug.rect.y,"images/projectiles/frost.png")
			direction()
		
	spawn(FPS, total_frames)
	collisions()

def spawn(FPS, total_frames):
	four_seconds = FPS * 4
	if total_frames % four_seconds == 0:
		r = random.randint(1, 2)
		# 50-50 chances of fly starting from either left or right
		x = 1
		if r == 2:
			x = 640 - 40


		classes.Fly(x, 130, "images/fly.png")

def collisions():
	for fly in classes.Fly.List:
		fly_proj = pygame.sprite.spritecollide(fly, classes.BugProjectile.List, True)
		if len(fly_proj ) > 0:
			for hit in fly_proj:
				fly.health -= fly.half_health

