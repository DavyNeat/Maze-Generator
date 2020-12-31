from maze import Maze
import pygame
import time
	
def getWalls(mainMaze):
	walls = []
	for y in range(mainMaze.height):
		for x in range(mainMaze.width):
			if(mainMaze.maze[y][x].walls['N']):
				walls.append(pygame.Rect(((width//mainMaze.width) * x), ((height//mainMaze.height) * y), (cell_width), (line_width)))
			if(mainMaze.maze[y][x].walls['E']):
				walls.append(pygame.Rect((((width//mainMaze.width) * x) + cell_width), ((height//mainMaze.height) * y), (line_width), (cell_height)))
			if(mainMaze.maze[y][x].walls['S']):
				walls.append(pygame.Rect(((width//mainMaze.width) * x), (((height//mainMaze.height) * y) + cell_height), (cell_width), (line_width)))
			if(mainMaze.maze[y][x].walls['W']):
				walls.append(pygame.Rect(((width//mainMaze.width) * x), ((height//mainMaze.height) * y), (line_width), (cell_height)))
	return walls
	
height, width = 1000, 1000
white = (255, 255, 255)
line = (0, 0, 0)
line_width = 5
moveSpeed = 1
playerX, playerY = 5, 5

mainMaze = Maze(50, 50)
cell_width, cell_height = width//mainMaze.width, height//mainMaze.height
mainMaze.populate_maze()
pygame.init()

pygame.display.set_caption('Maze Gen')
window = pygame.display.set_mode((width, height))

#TODO: Create rectangles for maze walls

sizeX, sizeY = cell_width//2, cell_height//2
walls = getWalls(mainMaze)


running = True

playerRect = pygame.Rect(playerX, playerY, sizeX, sizeY)

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
		if event.type == pygame.KEYDOWN:	
			if event.key == pygame.K_SPACE:
				mainMaze = Maze(50, 50)
				mainMaze.populate_maze()
				walls = getWalls(mainMaze)
	window.fill(white)
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and playerX > moveSpeed:
		playerX -= moveSpeed
	if keys[pygame.K_RIGHT] and playerX < width - sizeX - moveSpeed:
		playerX += moveSpeed
	if keys[pygame.K_UP] and playerY > moveSpeed:
		playerY -= moveSpeed
	if keys[pygame.K_DOWN] and playerY < height - sizeY - moveSpeed:
		playerY += moveSpeed
		
	wall = playerRect.collidelist(walls)
	constraint = 2
	for wall in walls:
		if playerRect.colliderect(wall):
			if abs(wall.top - playerRect.bottom) < constraint:
				#print('bottom')
				playerY -= moveSpeed
			if abs(wall.bottom - playerRect.top) < constraint:
				#print('top')
				playerY += moveSpeed
			if abs(wall.left - playerRect.right) < constraint:
				#print('right')
				playerX -= moveSpeed
			if abs(wall.right - playerRect.left) < constraint:
				#print('left')
				playerX += moveSpeed
		
	playerRect = pygame.Rect(playerX, playerY, sizeX, sizeY)
	
	pygame.draw.rect(window, (0, 0, 255), playerRect)
	for x in range(len(walls)):
		pygame.draw.rect(window, line, walls[x])
	pygame.display.update()


#TODO: Add solver and solving visualizer