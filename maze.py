import random

class Cell:
	def __init__(self, x, y):
		self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
		self.pairs = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
		self.x = x
		self.y = y
		self.visited = False
		
	def has_four_walls(self):
		return all(self.walls.values())
	
	def remove_wall(self, next_node, direction):
		self.walls[direction] = False
		next_node.walls[self.pairs[direction]] = False	
		
		
class Maze:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.maze = [[Cell(x, y) for x in range (0, width)] for y in range (0, height)]	
		
	def connected_cells(self, cell):
		cells = []
		directions = {'N':(-1, 0), 'E':(0, 1), 'S':(1, 0), 'W':(0, -1)}
		for direction in directions:
			x, y = cell.x + directions[direction][1], cell.y + directions[direction][0]
			if((x >= 0 and x < self.width) and (y >= 0 and y < self.height)):
				if(self.maze[y][x].has_four_walls()):
					cells.append((direction, self.maze[y][x]))
		return cells
	
	def populate_maze(self):
		stack = []
		#start = [0,0]
		start = [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]
		current = self.maze[start[0]][start[1]]
		stack.append(current)
		while stack:
			current = stack[len(stack) - 1]
			if(self.connected_cells(stack[len(stack) - 1])):
				direction, next_node = random.choice(self.connected_cells(stack[len(stack) - 1]))
				current.remove_wall(next_node, direction)
				current = next_node
				stack.append(current)
			else:
				stack.pop()
				
	#TODO: update to match the new Cell format that is being used
	"""
	def solveMaze(self):
		stack = []
		start = [0, 0]
		end = [self.width - 1, self.height - 1]
		solved = False
			
		while not solved:
			print()
	"""	
		
	
	def __str__ (self):
		maze_rows = ['-' * self.width * 2]
		for y in range(self.height):
			maze_row = ['|']
			for x in range(self.width):
				if self.maze[y][x].walls['E']:
					maze_row.append(' |')
				else:
					maze_row.append('  ')
			maze_rows.append(''.join(maze_row))
			maze_row = ['|']
			for x in range(self.width):
				if self.maze[y][x].walls['S']:
					maze_row.append('-+')
				else:
					maze_row.append(' +')
			maze_rows.append(''.join(maze_row))
		return '\n'.join(maze_rows)
