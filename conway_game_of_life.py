"""
__author__  = Willy Fitra Hendria
"""
import time

n_row = 101 # row size
n_col = 82 # col size
grid = [[ 0 for i in range(n_col)] for i in range(n_row)] # grid world
is_draw_grid = '1' # enum to display grid in the console or not (1 for draw, otherwise not draw)
n_living_cells = 0 # number of living cells
file_name = "result_"+time.strftime("%Y%m%d-%H%M%S")+".txt" # a file for storing number of living cells

# put initial pattern into the grid
def generate_initial_pattern(pattern, i_row, i_col):
	global n_living_cells
	if (pattern == '1'): # blinker
		grid[i_row][i_col] = 1
		grid[i_row+1][i_col] = 1
		grid[i_row+2][i_col] = 1
		n_living_cells = 3
	elif (pattern == '2'): # glider
		grid[i_row][i_col] = 1
		grid[i_row][i_col+1] = 1
		grid[i_row][i_col+2] = 1
		grid[i_row+1][i_col+2] = 1
		grid[i_row+2][i_col+1] = 1
		n_living_cells = 5
	elif (pattern == '3'): # r-pentomino
		grid[i_row][i_col+1] = 1
		grid[i_row][i_col+2] = 1
		grid[i_row+1][i_col] = 1
		grid[i_row+1][i_col+1] = 1
		grid[i_row+2][i_col+1] = 1
		n_living_cells = 5
	elif (pattern == '4'): # gosper's glider gun
		grid[i_row+4][i_col] = 1
		grid[i_row+5][i_col] = 1
		grid[i_row+4][i_col+1] = 1
		grid[i_row+5][i_col+1] = 1
		grid[i_row+4][i_col+10] = 1
		grid[i_row+5][i_col+10] = 1
		grid[i_row+6][i_col+10] = 1
		grid[i_row+3][i_col+11] = 1
		grid[i_row+7][i_col+11] = 1
		grid[i_row+2][i_col+12] = 1
		grid[i_row+8][i_col+12] = 1
		grid[i_row+2][i_col+13] = 1
		grid[i_row+8][i_col+13] = 1
		grid[i_row+5][i_col+14] = 1
		grid[i_row+3][i_col+15] = 1
		grid[i_row+7][i_col+15] = 1
		grid[i_row+4][i_col+16] = 1
		grid[i_row+5][i_col+16] = 1
		grid[i_row+6][i_col+16] = 1
		grid[i_row+5][i_col+17] = 1
		grid[i_row+2][i_col+20] = 1
		grid[i_row+3][i_col+20] = 1
		grid[i_row+4][i_col+20] = 1
		grid[i_row+2][i_col+21] = 1
		grid[i_row+3][i_col+21] = 1
		grid[i_row+4][i_col+21] = 1
		grid[i_row+1][i_col+22] = 1
		grid[i_row+5][i_col+22] = 1
		grid[i_row][i_col+24] = 1
		grid[i_row+1][i_col+24] = 1
		grid[i_row+5][i_col+24] = 1
		grid[i_row+6][i_col+24] = 1
		grid[i_row+2][i_col+34] = 1
		grid[i_row+3][i_col+34] = 1
		grid[i_row+2][i_col+35] = 1
		grid[i_row+3][i_col+35] = 1
		n_living_cells = 36
	elif (pattern == '5'): # lightweight spaceship
		grid[i_row+1][i_col] = 1
		grid[i_row][i_col+1] = 1
		grid[i_row+1][i_col+1] = 1
		grid[i_row+2][i_col+1] = 1
		grid[i_row][i_col+2] = 1
		grid[i_row+2][i_col+2] = 1
		grid[i_row+3][i_col+2] = 1
		grid[i_row+1][i_col+3] = 1
		grid[i_row+2][i_col+3] = 1
		grid[i_row+3][i_col+3] = 1
		grid[i_row+1][i_col+4] = 1
		grid[i_row+2][i_col+4] = 1
		n_living_cells = 12
		
# generate conway's game of life with torus boundary
def generate_cellular_automata():
	global n_living_cells
	global grid
	f = open(file_name, "a")
	f.write("total number of living cells for each time step (from step=0 to step="+ str(n_step) + "):\n\n")
	f.write(str(n_living_cells)+"\n") # write initial n_living_cells into a file
	draw(0)
	for step in range(n_step):
		next_grid = [[ 0 for i in range(n_col)] for i in range(n_row)]
		n_living_cells = 0;
		for i in range(n_row):
			for j in range(n_col):
				n_neighboors = 0;
				for k in [-1, 0, 1]:
					for l in [-1, 0, 1]:
						if (k != 0 or l != 0): # not a center cell
							m = i+k
							# overflow boundary
							if (m<0): 
								m=n_row-1
							elif (m == n_row):
								m=0
							
							n = j+l
							# overflow boundary
							if (n<0):
								n=n_col-1
							elif (n== n_col):
								n=0
							
							n_neighboors += grid[m][n]
							
				if (n_neighboors < 2): # loneliness
					next_grid[i][j] = 0
				elif (n_neighboors > 3): # overcrowding
					next_grid[i][j] = 0
				elif (n_neighboors == 3): # birth
					next_grid[i][j] = 1
				else: # keep the existing value or survival
					next_grid[i][j] = grid[i][j]
				
				n_living_cells += next_grid[i][j]
				
		f.write(str(n_living_cells)+"\n") # write n_living_cells into a file
		grid = next_grid
		draw(step+1)
	f.close()

# draw grid in the console
def draw(n_step):
	if (is_draw_grid == '1'):
		print("\ngrid pattern at step =", n_step)
		for i in range(n_row):
			for j in range(n_col):
				print('.' if (grid[i][j] == 0) else '*', end ="")
			print()

print("-----------------------")
print("Conway's Game of Life")
print("-----------------------")
print("1. blinker")
print("2. glider")
print("3. r-pentomino")
print("4. gosper's glider gun")
print("5. lightweight spaceship")
print()
selected_pattern =  input("Input the initial pattern ( 1 - 5 ):")
n_step = int(input("\nInput n of steps ( > 0 ):"))
is_draw_grid = input("\ndraw grid to console? (1. yes or 2. no):")

# generate initial pattern on a specified position
generate_initial_pattern (selected_pattern, int(n_row/2), int(n_col/2))

# generate cellular automata
generate_cellular_automata()

print("\nfile",file_name,"is created...\n")
print("total number of living cells for each time step are written into the file.")