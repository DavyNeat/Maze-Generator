from maze import Maze
import pygame
import time
	
height, width = 1000, 1000
white = (255, 255, 255)
line = (0, 0, 0)
line_width = 5
mainMaze = Maze(10, 10)
mainMaze.populate_maze()
pygame.init()

pygame.display.set_caption('Maze Gen')
window = pygame.display.set_mode((width, height))

running = True

while running:

	cell_width, cell_height = width//mainMaze.width, height//mainMaze.height
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.fill(white)
	for y in range(mainMaze.height):
		for x in range(mainMaze.width):
			if(mainMaze.maze[y][x].walls['N']):
				pygame.draw.line(window, line, ((width//mainMaze.width) * x, (height//mainMaze.height) * y), (((width//mainMaze.width) * x) + cell_width, (height//mainMaze.height) * y), line_width)
			if(mainMaze.maze[y][x].walls['E']):
				pygame.draw.line(window, line, (((width//mainMaze.width) * x) + cell_width, (height//mainMaze.height) * y), (((width//mainMaze.width) * x) + cell_width, ((height//mainMaze.height) * y) + cell_height), line_width)
			if(mainMaze.maze[y][x].walls['S']):
				pygame.draw.line(window, line, ((width//mainMaze.width) * x, ((height//mainMaze.height) * y) + cell_height), (((width//mainMaze.width) * x) + cell_width, ((height//mainMaze.height) * y) + cell_height), line_width)				
			if(mainMaze.maze[y][x].walls['W']):
				pygame.draw.line(window, line, ((width//mainMaze.width) * x, (height//mainMaze.height) * y), ((width//mainMaze.width) * x, ((height//mainMaze.height) * y) + cell_height), line_width)
				
	pygame.display.update()


#TODO: Add player dot to solve the maze
#TODO: Add solver and solving visualizer