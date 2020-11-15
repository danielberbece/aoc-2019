
import time
from os import system

def getMem():
	f = open('13.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array


def checkExtend(array, pos):
	while pos >= len(array):
		array.append(0)

def print_map():
	global mm
	# print(mm)
	minx = 0
	maxx = 0
	miny = 0
	maxy = 0

	for pos in mm:
		if pos[0] > maxx:
			maxx = pos[0]
		if pos[0] < minx:
			minx = pos[0]
		if pos[1] > maxy:
			maxy = pos[1]
		if pos[1] < miny:
			miny = pos[1]
	for y in range(miny, maxy):
		for x in range(minx, maxx + 1):
			if (x,y) in mm:
				if mm[(x,y)] == 0:
					print(" ", end="")
				elif mm[(x,y)] == 1:
					print("|", end="")
				elif mm[(x,y)] == 2:
					print("#", end="")
				elif mm[(x,y)] == 3:
					print("=", end="")
				elif mm[(x,y)] == 4:
					print("0", end="")
				else:
					print(" ", end="")
			else:
				print(" ", end="")
		print("")



i = 0
relative_i = 0
in_pos = 0

def run(array, inputs):
	global i, relative_i, in_pos, ball_x, pad_x, prev_ball_x
	outputs = []
	while True:
		# take instruction
		if array[i] % 100 == 1:
			#add
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				checkExtend(array,relative_i + array[i + 3])
				array[relative_i + array[i + 3]] = p1 + p2
			else:
				array[array[i + 3]] = p1 + p2
			i += 4
		elif array[i] % 100 == 2:	 # multiply
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				checkExtend(array,relative_i + array[i + 3])
				array[relative_i + array[i + 3]] = p1 * p2
			else:
				array[array[i + 3]] = p1 * p2
			i += 4
		elif array[i] % 100 == 3:
			checkExtend(array, i + 1)
			system('clear')
			print_map()
			time.sleep(0.05)
			val = 0
			# print(prev_ball_x, ball_x, pad_x)
			if prev_ball_x < ball_x and ball_x > pad_x:
				val = 1
			elif prev_ball_x > ball_x and ball_x < pad_x:
				val = -1

			if (array[i] // 10000) % 10 == 2:
				checkExtend(array, relative_i + array[i + 1])
				array[relative_i + array[i + 1]] = val
			else:
				array[array[i + 1]] = val
			in_pos += 1
			i += 2
		elif array[i] % 100 == 4:
			p1 = getParam(array, i, 1, relative_i)
			outputs.append(p1)
			i += 2
			if len(outputs) == 3:
				return True, outputs
		elif array[i] % 100 == 5:	# jump if true
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			if p1 != 0:
				i = p2
			else:
				i += 3
		elif array[i] % 100 == 6:	# jump if false
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			if p1 == 0:
				i = p2
			else:
				i += 3			
		elif array[i] % 100 == 7:	# less than
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			store_val = 0
			if p1 < p2:
				store_val = 1
	
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				array[relative_i + array[i + 3]] = store_val
			else:
				array[array[i + 3]] = store_val
			i += 4			
		elif array[i] % 100 == 8:	# eq
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			store_val = 0
			if p1 == p2:
				store_val = 1
	
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				array[relative_i + array[i + 3]] = store_val
			else:
				array[array[i + 3]] = store_val
			i += 4
		elif array[i] % 100 == 9:
			p1 = getParam(array, i, 1, relative_i)
			relative_i += p1
			i += 2
		elif array[i] % 100 == 99:
			break
		else:

			print('Wrong instruction', array[i], i)
			exit(-1)
		
	return False, []

def getParam(array, i, offset, relative):
	p1 = array[i + offset]
	if (array[i] // ((10 ** offset) * 10)) % 10 == 0:
		if p1 >= len(array):
			p1 = 0
		else:
			p1 = array[p1]
	elif (array[i] // ((10 ** offset) * 10)) % 10 == 2:
		if p1 >= len(array):
			p1 = 0
		else:
			p1 = array[relative + p1]

	return p1

mem = getMem()
running = True
mm = {}
cnt_block_tiles = 0
ball_x = 0
pad_x = 0
prev_ball_x = 0
inputs = [0]
while running:
	running, outputs = run(mem, inputs)
	if not running:
		break
	posx = (outputs[0], outputs[1])
	mm[posx] = outputs[2]
	if outputs[2] == 4:
		prev_ball_x = ball_x
		ball_x = outputs[0]
	elif outputs[2] == 3:
		pad_x = outputs[0]
	elif outputs[2] == 2:
		cnt_block_tiles += 1
# print('part 1:', cnt_block_tiles)
print_map()
print(mm[(-1,0)])



# while running:
# 	curr_color = 0
# 	if pos in mm:
# 		curr_color = mm[pos]
# 	running, outputs = run(mem, [curr_color])
# 	if not running:
# 		break
# 	mm[pos] = outputs[0]
# 	if direction == 0:
# 		if outputs[1] == 0:
# 			pos = (pos[0] - 1, pos[1])
# 			direction = 1
# 		elif outputs[1] == 1:
# 			pos = (pos[0] + 1, pos[1])
# 			direction = 3
# 	elif direction == 1:
# 		if outputs[1] == 0:
# 			pos = (pos[0], pos[1] - 1)
# 			direction = 2
# 		elif outputs[1] == 1:
# 			pos = (pos[0], pos[1] + 1)
# 			direction = 0
# 	elif direction == 2:
# 		if outputs[1] == 0:
# 			pos = (pos[0] + 1, pos[1])
# 			direction = 3
# 		elif outputs[1] == 1:
# 			pos = (pos[0] - 1, pos[1])
# 			direction = 1
# 	elif direction == 3:
# 		if outputs[1] == 0:
# 			pos = (pos[0], pos[1] + 1)
# 			direction = 0
# 		elif outputs[1] == 1:
# 			pos = (pos[0], pos[1] - 1)
# 			direction = 2



