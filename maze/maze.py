import random

#cells will be used to populate the maze
class Cell:
	def __init__(self, x, y):
		self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
		self.pairs = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
		self.x = x
		self.y = y
		self.visited = False
		self.correct = False
		
	#checks if the cell has had any walls removed while generating a maze
	def has_four_walls(self):
		return all(self.walls.values())
	
	#removes walls from the cell when generating a maze
	def remove_wall(self, next_node, direction):
		self.walls[direction] = False
		next_node.walls[self.pairs[direction]] = False	
		
		
class Maze:
	#creates a maze with an initial height and width, then populates it with cells
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.solved = False
		self.maze = [[Cell(x, y) for x in range (0, width)] for y in range (0, height)]	
		
	#checks connected cells and returns a list of cells that have not been visited during generation
	def connected_full_cells(self, cell):
		cells = []
		directions = {'N':(-1, 0), 'E':(0, 1), 'S':(1, 0), 'W':(0, -1)}
		for direction in directions:
			x, y = cell.x + directions[direction][1], cell.y + directions[direction][0]
			if((x >= 0 and x < self.width) and (y >= 0 and y < self.height)):
				if(self.maze[y][x].has_four_walls()):
					cells.append((direction, self.maze[y][x]))
		return cells
	#checks connected cells and returns a list of cells that have not been visited while solving
	def possible_paths(self, cell):
		cells = []
		directions = {'N':(-1, 0), 'E':(0, 1), 'S':(1, 0), 'W':(0, -1)}
		for direction in directions:
			x, y = cell.x + directions[direction][1], cell.y + directions[direction][0]
			if((x >= 0 and x < self.width) and (y >= 0 and y < self.height)):
				if(not self.maze[y][x].walls[self.maze[y][x].pairs[direction]] and not self.maze[y][x].visited):
					cells.append(self.maze[y][x])
		return cells
	
	#starts populating maze from a random point and backtracks when there are no more connected cells that have not been visited
	def populate_maze(self):
		stack = []
		start = [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]
		stack.append(self.maze[start[0]][start[1]])
		while stack:
			current = stack[len(stack) - 1]
			if(self.connected_full_cells(current)):
				direction, next_node = random.choice(self.connected_full_cells(current))
				current.remove_wall(next_node, direction)
				stack.append(next_node)
			else:
				stack.pop()
	
	#solves the maze in the same way that it was populated, but instead backtracks when the connected cells have been visited or have a wall blocking the path
	def solveMazeDF(self):
		stack = []
		self.maze[0][0].visited, self.maze[0][0].correct = True, True
		stack.append(self.maze[0][0])
		while not self.solved:
			current = stack[len(stack) - 1]
			if(self.possible_paths(current)):
				next_node = random.choice(self.possible_paths(current))
				next_node.correct, next_node.visited = True, True
				stack.append(next_node)
			else:
				current.correct = False
				stack.pop()
			if(self.height - 1 == stack[len(stack) - 1].y and self.width - 1 == stack[len(stack) - 1].x):
				self.solved = True
