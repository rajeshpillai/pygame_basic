import pygame

class BaseClass(pygame.sprite.Sprite):
	allsprites = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_string):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.width = width
		self.height = height

class Bug(BaseClass):
	List = pygame.sprite.Group()
	
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width,height, image_string)
		Bug.List.add(self)
		self.velx, self.vely = 0, 5
		self.jumping, self.go_down = False, False


	def motion(self, SCREENWIDTH, SCREENHEIGHT):
		predicted_location = self.rect.x + self.velx
		
		if predicted_location < 0:
			self.velx = 0
		elif  predicted_location + self.width > SCREENWIDTH:
			self.velx = 0
		
		self.rect.x += self.velx

		self.__jump(SCREENHEIGHT)

	def __jump(self,SCREENHEIGHT):

		max_jump = 75

		if self.jumping:
			if self.rect.y < max_jump:
				self.go_down = True

			if self.go_down:
				self.rect.y += self.vely
				predicted_location = self.rect.y + self.vely

				if predicted_location + self.height > SCREENHEIGHT:
					self.jumping = False
					self.go_down = False

			else:
				self.rect.y -= self.vely
