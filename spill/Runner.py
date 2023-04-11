import pygame
from sys import exit					
from random import randint, choice

class Spiller(pygame.sprite.Sprite): #sprite er en classe som inneholder overflate og rektangel 
	def __init__(self):
		super().__init__()
		spiller_walk_1 = pygame.image.load('grafikk/Spiller/spiller_walk_1.png').convert_alpha()
		spiller_walk_2 = pygame.image.load('grafikk/Spiller/spiller_walk_2.png').convert_alpha() #her henter jeg bildene til person 
		self.spiller_walk = [spiller_walk_1,spiller_walk_2]
		self.spiller_index = 0
		self.spiller_jump = pygame.image.load('grafikk/spiller/spiller_hop.png').convert_alpha()
		self.spiller_krab = pygame.image.load('grafikk/spiller/spiller_krab.png').convert_alpha()

		self.image = self.spiller_walk[self.spiller_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0	
 
	def animation_state(self):
		if self.rect.bottom < 300: #ser om spilleren hopper
			self.image = self.spiller_jump
		else:
			self.spiller_index += 0.1 #endrer bilde til spilleren for å lage en gå animasjon 
			if self.spiller_index >= len(self.spiller_walk):	
				self.spiller_index = 0 
			self.image = self.spiller_walk[int(self.spiller_index)]
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_s] and self.rect.bottom >= 300:	#får spiller til å krabbe
			self.image = self.spiller_krab

	def spiller_input(self): #hoppe knap
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
		if keys[pygame.K_w] and self.rect.bottom >= 300:
			self.gravity = -20

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def update(self): #opptaterer son at animaskjonen spiller
		self.spiller_input()
		self.apply_gravity()
		self.animation_state()

class Hindring(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'bat':
			bat1 = pygame.image.load('grafikk/flagermus/flagermus1.png').convert_alpha()		
			bat2 = pygame.image.load('grafikk/flagermus/flagermus2.png').convert_alpha()
			self.frames = [bat1,bat2]
			y_pos = 210
		elif type == 'zombi':
			zombi_1 = pygame.image.load('grafikk/Zombi/zombi_1.png').convert_alpha()
			zombi_2 = pygame.image.load('grafikk/Zombi/zombi_2.png').convert_alpha()
			self.frames = [zombi_1,zombi_2]
			y_pos  = 300
		else:
			zombi_1 = pygame.image.load('grafikk/flagermus/spokelse.png').convert_alpha()
			zombi_2 = pygame.image.load('grafikk/flagermus/spokelse.png').convert_alpha()
			self.frames = [zombi_1,zombi_2]
			y_pos  = 216

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 #bytter bilde til hindringer får å få det til å se ut som animasjon
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6	#beveger hindringer 
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: #ødlegger hindringer hvis de går for langt til venstre
			self.kill()


def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))		#er en timer som tar tiden i ms og deller den på tusen
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def collision_sprite():
	if pygame.sprite.spritecollide(spiller.sprite,obstacle_group,False):	
		obstacle_group.empty()	#sletter hindringer
		return False
	else: return True

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
game_active = False
start_time = 0
current_time = 0
score = 0

spiller = pygame.sprite.GroupSingle()
spiller.add(Spiller())

obstacle_group = pygame.sprite.Group()

ground_surface = pygame.image.load('grafikk/bakgrunn/bakke.png').convert()

# Himmel
himmel1 = pygame.image.load("grafikk/bakgrunn/himmel.png").convert_alpha()	#importerer himmel
himmel1_rect = himmel1.get_rect(topleft = (800,0))
himmel2 = pygame.image.load("grafikk/bakgrunn/himmel.png").convert_alpha()
himmel2_rect = himmel2.get_rect(topleft = (0,0))
himmel3 = pygame.image.load("grafikk/bakgrunn/himmel.png").convert_alpha()
himmel3_rect = himmel3.get_rect(topleft = (-800,0))

#sky1 = pygame.image.load("grafikk/bakgrunn/sky1.png").convert_alpha()
#sky2 = pygame.image.load("grafikk/bakgrunn/sky2.png").convert_alpha()
#sky3 = pygame.image.load("grafikk/bakgrunn/sky3.png").convert_alpha()
#sky1_x_pos = 600
#sky2_x_pos = 600
#sky3_x_pos = 600

obstacle_rect_list = []

# Intro screen
spiller_stand = pygame.image.load('grafikk/Spiller/spiller_stand.png').convert_alpha()
spiller_stand = pygame.transform.rotozoom(spiller_stand,0,2)
spiller_stand_rect = spiller_stand.get_rect(center = (400,200))

# Klokke 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1200)	#her er timeren til når hindringer blir satt ut

#sky_timer = pygame.USEREVENT + 1
#pygame.time.set_timer(sky_timer,1200)

game_name = test_font.render('Runner',False,(111,196,169))	#text på skjemmen når spille ikke er aktivt
game_name_rect = game_name.get_rect(center = (400,80))
game_score_imput = test_font.render('lagre score trykk h',False,(111,196,169))
game_score_rect = game_score_imput.get_rect(center = (600,80))
game_message = test_font.render('Trykk mellomrom fortsette',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

#mycursor = mydb.curor()
#mycursor.execute("SELECT name, address FROM customers")
#myresult = mycursor.fetchall()
#for x in myresult:
#	print (x)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if game_active:
			pass
			
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:	#starter spillet
				game_active = True
				
				start_time = int(pygame.time.get_ticks() / 1000)

		#viser himmelen bevege seg
		himmel1_rect.x -=1
		if himmel1_rect.right <= -800: himmel1_rect.left = 800
		himmel2_rect.x -=1
		if himmel2_rect.right <= -800: himmel2_rect.left = 800
		himmel3_rect.x -=1
		if himmel3_rect.right <= -800: himmel3_rect.left = 800 

		#if game_active:
		#	if event.type == obstacle_timer:
		#		((choice(['sky1','sky2','sky3'])))


		if event.type == obstacle_timer:
			obstacle_group.add(Hindring(choice(['bat','bat','spokelse','zombi','zombi','zombi'])))  	#her er koden som sponer hindringer

	if game_active:
		#det som blir vist på skjermen
		screen.blit(ground_surface,(0,300))
		screen.blit(himmel1,himmel1_rect)
		screen.blit(himmel3,himmel2_rect)	#viser ale bakgrunnene
		screen.blit(himmel3,himmel3_rect)

		score = display_score()
		spiller.draw(screen)  #viser spiller
		spiller.update()

		obstacle_group.draw(screen) #viser hindringer
		obstacle_group.update()

		game_active = collision_sprite() #komiserer med fuksjonen collision får å slutte spillet

	else:
		screen.fill((255,0,0))
		screen.blit(spiller_stand,spiller_stand_rect)

		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

		

		if score == 0: 				#bestemer om set skal stå score eller mellom rom får å forsette
			screen.blit(game_message,game_message_rect)
		else: 
			screen.blit(score_message,score_message_rect)
			screen.blit(game_score_imput,game_score_rect) #	her kan jeg skrive navn
			keys = pygame.key.get_pressed() 
		#help = pygame.image.load("grafikk/help.png")
		#help_pos = help.get_rect(topleft = (0,0))
		#keys = pygame.key.get_pressed() 
		#if keys[pygame.K_h]:
		#	screen.blit(help)


	pygame.display.update()
	clock.tick(60)