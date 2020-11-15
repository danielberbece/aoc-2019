import sys

def getMem():
	f = open('15.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array

i = 0
relative_i = 0
def run(array, inputs, reset=False):
	global i, relative_i
	if reset:
		i = 0
		relative_i = 0
	in_pos = 0
	while True:
		# take instruction
		if array[i] % 100 == 1:
			#add
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			
			saveValue(array, i, 3, relative_i, p1 + p2)
			i += 4
		elif array[i] % 100 == 2:	 # multiply
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			
			saveValue(array, i, 3, relative_i, p1 * p2)
			i += 4
		elif array[i] % 100 == 3:
			saveValue(array, i, 1, relative_i, inputs[in_pos])
			in_pos += 1
			i += 2
		elif array[i] % 100 == 4:
			p1 = getParam(array, i, 1, relative_i)
			i += 2
			return True, p1
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

			saveValue(array, i, 3, relative_i, store_val)
			i += 4			
		elif array[i] % 100 == 8:	# eq
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			store_val = 0
			if p1 == p2:
				store_val = 1
	
			saveValue(array, i, 3, relative_i, store_val)
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
		
	return False, -1

def getParam(array, i, offset, relative):
	p1 = array[i + offset]
	if (array[i] // ((10 ** offset) * 10)) % 10 == 0:
		p1 = array[p1]
	elif (array[i] // ((10 ** offset) * 10)) % 10 == 2:
		p1 = array[relative + p1]

	return p1

def saveValue(array, i, offset, relative, value):
	if (array[i] // ((10 ** offset) * 10)) % 10 == 2:
		array[relative + array[i + offset]] = value
	else:
		array[array[i + offset]] = value

def print_map(mm):
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
				if (x, y) == (0,0):
					print("S", end="")
				if mm[(x,y)] == 0:
					print("#", end="")
				elif mm[(x,y)] == 1:
					print(".", end="")
				elif mm[(x,y)] == 2:
					print("@", end="")
				else:
					print(" ", end="")
			else:
				print("?", end="")
		print("")


next_p = {1: (0, 1), 2: (0, -1), 3:(-1,0), 4: (1, 0)}
opposite_dir = {1: 2, 2: 1, 3: 4, 4: 3}
steps = 0

def add_tuples(t1, t2):
	return tuple(map(lambda x, y: x + y, t1, t2))

def search(pos):
	global prog, mapp, next_p, opposite_dir, steps, oxygen_pos
	# print(steps, pos)
	if pos in mapp and mapp[pos] == 1:
		for direction in range(1,5):
			if add_tuples(pos, next_p[direction]) in mapp:
				continue
			_, output = run(prog, [direction])
			mapp[add_tuples(pos, next_p[direction])] = output
			if output == 0:
				continue
			elif output == 1:
				steps += 1
				search(add_tuples(pos, next_p[direction]))
				run(prog, [opposite_dir[direction]])
				steps -= 1
			elif output == 2:
				steps += 1
				print("Part1: reached oxygen in %d steps"%steps)
				oxygen_pos = add_tuples(pos, next_p[direction])
				search(add_tuples(pos, next_p[direction]))
				run(prog, [opposite_dir[direction]])
				steps -= 1
			else:
				print("wrong output: ", output)
				exit(-1) 

def fill(pos):
	global mapp
	time = 0
	Q = [(pos, 0)]
	visited = {pos: 1}
	while len(Q) > 0:
		elem = Q.pop(0)
		if time < elem[1]:
			time = elem[1]
		for direction in range(1,5):
			next_position= add_tuples(elem[0], next_p[direction])
			if mapp[next_position] == 1 and next_position not in visited:
				visited[next_position] = 1
				Q.append((next_position, elem[1] + 1))

	print("Part2: Time taken to will with oxygen:", time)


sys.setrecursionlimit(10**6) 
oxygen_pos = (0,0)

#part 1
prog = getMem() + 10000*[0]
mapp = {(0,0):1}
search((0,0))

#part 2
fill(oxygen_pos)
