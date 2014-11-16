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
	if keys[pygame.K_RIGHT]:
		classes.Bug.going_right = True
		bug.image = pygame.image.load("images/bug.png")
		bug.velx = 5
	elif keys[pygame.K_LEFT]:
		classes.Bug.going_right = False
		bug.image = pygame.image.load("images/bugflipped.png")
		bug.velx = -5
	else:
		bug.velx = 0


	# Vertical movement
	if keys[pygame.K_UP]:
		bug.jumping = True

	if keys[pygame.K_SPACE]:
		def direction():
			if classes.Bug.going_right:
				p.velx = 8
			else:
				p.image = pygame.transform.flip(p.image, True, False) # flip horizontally
				p.velx = -8

		if (classes.BugProjectile.fire):
			p = classes.BugProjectile(bug.rect.x, bug.rect.y, True,"images/projectiles/fire.png")
			direction()
		else:
			p = classes.BugProjectile(bug.rect.x, bug.rect.y,False,"images/projectiles/frost.png")
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
	# freeze flies
	# width px projectiles

#	for fly in classes.Fly.List:
#		if pygame.sprite.spritecollide(fly, classes.BugProjectile.List, False):
#			if classes.BugProjectile.fire:
#				fly.health -= fly.half_health
#			else:
#				fly.velx = 0
#
#	for proj in classes.BugProjectile.List:
#		if pygame.sprite.spritecollide(proj, classes.Fly.List, False):
#			proj.rect.x = 2 * -proj.rect.width
#			proj.destroy()

    for fly in classes.Fly.List:
        projectiles = pygame.sprite.spritecollide(fly,classes.BugProjectile.List, True)
        
        for projectile in projectiles:
        	fly.health = 0  # We killed a lfy

        	if projectile.isFire:
        		fly.image = pygame.image.load("images/burnt_fly.png")
        	else:
        		if fly.velx > 0:
        			fly.image = pygame.image.load("images/frozen_fly.png")
        		elif fly.velx < 0:
        			fly.image = pygame.image.load("images/frozen_fly.png")
        			fly.image = pygame.transform.flip(fly.image, True, False)
    		
    		projectile.rect.x = 2 * -projectile.rect.width
    		projectile.destroy()


