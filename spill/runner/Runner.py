import pygame
import sys
import os
from random import randint, choice

grafikk_dir = os.path.join(sys.path[0], 'grafikk')
spiller_dir = os.path.join(grafikk_dir, 'Spiller')
skrift_dir = os.path.join(grafikk_dir, 'font')

class Spiller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        spiller_walk_1 = pygame.image.load(os.path.join(spiller_dir, 'spiller_walk_1.png')).convert_alpha()
        spiller_walk_2 = pygame.image.load(os.path.join(spiller_dir, 'spiller_walk_2.png')).convert_alpha()
        self.spiller_walk = [spiller_walk_1, spiller_walk_2]
        self.spiller_index = 0
        self.spiller_jump = pygame.image.load(os.path.join(spiller_dir, 'spiller_hop.png')).convert_alpha()

        self.image = self.spiller_walk[self.spiller_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

    def spiller_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            # self.jump_sound.play()  # Uncomment if jump sound is available

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.spiller_jump
        else:
            self.spiller_index += 0.1
            if self.spiller_index >= len(self.spiller_walk):
                self.spiller_index = 0
            self.image = self.spiller_walk[int(self.spiller_index)]

    def update(self):
        self.spiller_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        flagermus_dir = os.path.join(grafikk_dir, 'flagermus')
        zombi_dir = os.path.join(grafikk_dir, 'Zombi')

        if type == 'fly':
            fly_1 = pygame.image.load(os.path.join(flagermus_dir, 'flagermus1.png')).convert_alpha()
            fly_2 = pygame.image.load(os.path.join(flagermus_dir, 'flagermus1.png')).convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load(os.path.join(zombi_dir, 'Zombi_1.png')).convert_alpha()
            snail_2 = pygame.image.load(os.path.join(zombi_dir, 'Zombi_1.png')).convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()


def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def obstacle_movement(obstacle_list):
	if obstacle_list:
		for obstacle_rect in obstacle_list:
			obstacle_rect.x -= 5

			if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)
			else: screen.blit(fly_surf,obstacle_rect)

		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

		return obstacle_list
	else: return []

def collisions(spiller,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if spiller.colliderect(obstacle_rect): return False
	return True

def collision_sprite():
	if pygame.sprite.spritecollide(spiller.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

def spiller_animation():
	global spiller_surf, spiller_index

	if spiller_rect.bottom < 300:
		spiller_surf = spiller_jump
	else:
		spiller_index += 0.1
		if spiller_index >= len(spiller_walk):spiller_index = 0
		spiller_surf = spiller_walk[int(spiller_index)]

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(os.path.join(skrift_dir, 'Pixeltype.ttf'))
game_active = False
start_time = 0
score = 0

#Groups
spiller = pygame.sprite.GroupSingle()
spiller.add(spiller())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Snail 
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


spiller_walk_1 = pygame.image.load('graphics/spiller/spiller_walk_1.png').convert_alpha()
spiller_walk_2 = pygame.image.load('graphics/spiller/spiller_walk_2.png').convert_alpha()
spiller_walk = [spiller_walk_1,spiller_walk_2]
spiller_index = 0
spiller_jump = pygame.image.load('graphics/spiller/jump.png').convert_alpha()

spiller_surf = spiller_walk[spiller_index]
spiller_rect = spiller_surf.get_rect(midbottom = (80,300))
spiller_gravity = 0

# Intro screen
spiller_stand = pygame.image.load('graphics/spiller/spiller_stand.png').convert_alpha()
spiller_stand = pygame.transform.rotozoom(spiller_stand,0,2)
spiller_stand_rect = spiller_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if spiller_rect.collidepoint(event.pos) and spiller_rect.bottom >= 300: 
					spiller_gravity = -20
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and spiller_rect.bottom >= 300:
					spiller_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				
				start_time = int(pygame.time.get_ticks() / 1000)

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
				# if randint(0,2):
				# 	obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
				# else:
				# 	obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

			if event.type == snail_animation_timer:
				if snail_frame_index == 0: snail_frame_index = 1
				else: snail_frame_index = 0
				snail_surf = snail_frames[snail_frame_index] 

			if event.type == fly_animation_timer:
				if fly_frame_index == 0: fly_frame_index = 1
				else: fly_frame_index = 0
				fly_surf = fly_frames[fly_frame_index] 


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		# pygame.draw.rect(screen,'#c0e8ec',score_rect)
		# pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
		# screen.blit(score_surf,score_rect)
		score = display_score()
		
		# snail_rect.x -= 4
		# if snail_rect.right <= 0: snail_rect.left = 800
		# screen.blit(snail_surf,snail_rect)

		# spiller 
		# spiller_gravity += 1
		# spiller_rect.y += spiller_gravity
		# if spiller_rect.bottom >= 300: spiller_rect.bottom = 300
		# spiller_animation()
		# screen.blit(spiller_surf,spiller_rect)
		spiller.draw(screen)
		spiller.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		# Obstacle movement 
		# obstacle_rect_list = obstacle_movement(obstacle_rect_list)

		# collision 
		game_active = collision_sprite()
		# game_active = collisions(spiller_rect,obstacle_rect_list)
		
	else:
		screen.fill((94,129,162))
		screen.blit(spiller_stand,spiller_stand_rect)
		obstacle_rect_list.clear()
		spiller_rect.midbottom = (80,300)
		spiller_gravity = 0

		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)