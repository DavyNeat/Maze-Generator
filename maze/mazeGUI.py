from maze import Maze
import pygame
import time
	
def getWalls(mainMaze):
	#makes and returns a list of all the walls in the maze as rectangles
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
cellsX, cellsY = 50, 50

mainMaze = Maze(cellsX, cellsY)
cell_width, cell_height = width//mainMaze.width, height//mainMaze.height
mainMaze.populate_maze()

pygame.init()
pygame.display.set_caption('Maze Gen')
window = pygame.display.set_mode((width, height))

sizeX, sizeY = cell_width//3, cell_height//3
walls = getWalls(mainMaze)

playerRect = pygame.Rect(playerX, playerY, sizeX, sizeY)

running = True
while running:
	#Checks if the window is closed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#Checks if the space button is pressed to generate a maze and the enter key to solve it
		if event.type == pygame.KEYDOWN:	
			if event.key == pygame.K_SPACE:
				mainMaze = Maze(cellsX, cellsY)
				cell_width, cell_height = width//mainMaze.width, height//mainMaze.height
				mainMaze.populate_maze()
				walls = getWalls(mainMaze)
				playerX, playerY = 5, 5
				sizeX, sizeY = cell_width//3, cell_height//3
			if event.key == pygame.K_RETURN:
				mainMaze.solveMaze()
				
	window.fill(white)
		
	#colors the path to the end of the maze green when it is solved
	if(mainMaze.solved):
		for y in range(mainMaze.height):
			for x in range(mainMaze.width):
				if(mainMaze.maze[y][x].correct):
					correctRect = pygame.Rect(cell_width * x, cell_height * y, cell_width, cell_height)
					pygame.draw.rect(window, (0, 255, 0), correctRect)
	keys = pygame.key.get_pressed()

	#moves player square
	if keys[pygame.K_LEFT] and playerX > moveSpeed:
		playerX -= moveSpeed
	if keys[pygame.K_RIGHT] and playerX < width - sizeX - moveSpeed:
		playerX += moveSpeed
	if keys[pygame.K_UP] and playerY > moveSpeed:
		playerY -= moveSpeed
	if keys[pygame.K_DOWN] and playerY < height - sizeY - moveSpeed:
		playerY += moveSpeed
		
	#checks for collisions
	#TODO: add and extra check for key press
	wall = playerRect.collidelist(walls)
	constraint = 2
	for wall in walls:
		if playerRect.colliderect(wall):
			if abs(wall.top - playerRect.bottom) < constraint:
				playerY -= moveSpeed
			if abs(wall.bottom - playerRect.top) < constraint:
				playerY += moveSpeed
			if abs(wall.left - playerRect.right) < constraint:
				playerX -= moveSpeed
			if abs(wall.right - playerRect.left) < constraint:
				playerX += moveSpeed
		
	playerRect = pygame.Rect(playerX, playerY, sizeX, sizeY)
	pygame.draw.rect(window, (255, 0, 0), playerRect)
	#draws maze walls
	for x in range(len(walls)):
		pygame.draw.rect(window, line, walls[x])
	pygame.display.update()