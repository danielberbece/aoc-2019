import time
from os import system

def getMem():
	f = open('19.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array


def run(array, inputs, xasdf):
	i = 0
	relative_i = 0
	in_pos = 0
	outputs = []
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
			outputs.append(p1)
			i += 2
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
		
	return False, outputs

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


#Part 1
side = 50
cnt = 0
for i in range(side):
	for j in range(side):
		r, output = run(getMem() + 10000*[0], [j, i], True)
		if output[0] == 1:
			cnt += 1
print("part1:",cnt)

#PART 2

x_left = 0
x_right = 1 

ranges = []
i = 0
while True:
	curr_min = 9999999999
	cnt = 0
	for j in range(x_left, x_right):
		r, output = run(getMem() + 10000*[0], [j, i], True)
		if output[0] == 1:
			if curr_min > j:
				curr_min = j
			cnt += 1
	if (curr_min != 9999999999):
		x_left = curr_min
		x_right = x_left + cnt + 5
	ranges.append((x_left, x_right - 5))
	i +=1
	if i >= 100:
		if cnt >= 100 and ranges[-100][1] - x_left >= 100:
			print("part2:", x_left * 10000 + i - 100)
			break




