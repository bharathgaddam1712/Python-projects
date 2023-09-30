# importing libraries
from IPython.display import Audio
import pygame
import time
import random

snake_speed = 25
fruit_spawn_time = time.time()


window_x = 1024
window_y = 640

apple_image = pygame.image.load('apple.jpg')
snake_color = pygame.Color(0, 255, 0)
apple_image = pygame.transform.scale(apple_image, (15, 15))
snake_color = pygame.Color(0,0,0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
top_color = (135, 206, 235)  
bottom_color = (0, 0, 128)



pygame.init()

sound_file = 'eat.mp3'

pygame.display.set_caption('Snakes Game')
game_window = pygame.display.set_mode((window_x, window_y))


fps = pygame.time.Clock()


snake_position = [100, 50]


snake_body = [[150, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]

fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True


direction = 'RIGHT'
change_to = direction


score = 0


def show_score(choice, color, font, size, time_string=None):
	if time_string is not None:



		score_font = pygame.font.SysFont(font, size)

		score_surface = score_font.render('Score : ' + str(score), True, color)


		score_rect = score_surface.get_rect()

		game_window.blit(score_surface, score_rect)
    
def game_over():

	my_font = pygame.font.SysFont('times new roman', 50)

	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	

	game_over_rect = game_over_surface.get_rect()
	

	game_over_rect.midtop = (window_x/2, window_y/4)

	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()

	restart_font = pygame.font.SysFont('times new roman', 30)
	restart_surface = restart_font.render('Press R to Restart', True, blue)
	restart_rect = restart_surface.get_rect()
	restart_rect.midtop = (window_x / 2, window_y / 2)
	game_window.blit(restart_surface, restart_rect)
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:

					main()
				if event.key == pygame.K_q:

					pygame.quit()
					quit()
start_time = time.time()                    
                    
                    
while True:
                    


    
	elapsed_time = time.time() - fruit_spawn_time    
	if elapsed_time > 10:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,random.randrange(1, (window_y//10)) * 10]    
		fruit_spawn_time = time.time()     
    
    
	current_time = time.time() - start_time
	time_string = "Time: {:.2f}".format(current_time)

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'




	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'


	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10
        
      
	if snake_position[0] >= window_x:
		snake_position[0] = 0
	elif snake_position[0] < 0:
		snake_position[0] = window_x - 10
	if snake_position[1] >= window_y:
		snake_position[1] = 0
	elif snake_position[1] < 0:
		snake_position[1] = window_y - 10
        

	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	gradient_color = (
		int(top_color[0] + (bottom_color[0] - top_color[0]) * pos[1] / window_y),
		int(top_color[1] + (bottom_color[1] - top_color[1]) * pos[1] / window_y),
		int(top_color[2] + (bottom_color[2] - top_color[2]) * pos[1] / window_y))
	game_window.fill(gradient_color)    

	for pos in snake_body:
		pygame.draw.rect(game_window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))  
	game_window.blit(apple_image, (fruit_position[0], fruit_position[1])) 
    
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
		display(Audio(sound_file, autoplay=True))                       

	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	show_score(1, white, 'times new roman', 20)
	show_score(2, white, 'times new roman', 20, time_string)    
    
 
	pygame.display.update()
    
    

	fps.tick(snake_speed)
                    
                    




