
def getMem():
	array = []
	f = open('02.txt', 'r')
	text = f.readline()
	while text:
		array.append(int(text))
		text = f.readline()
	return array

def run(array):
	i = 0
	while True:
		# take instruction
		if array[i] == 1:
			#add
			array[array[i + 3]] = array[array[i + 1]] + array[array[i + 2]]
		elif array[i] == 2:
			array[array[i + 3]] = array[array[i + 1]] * array[array[i + 2]]
		elif array[i] == 99:
			break
		else:
			print('Wrong instruction', i)
			exit(-1)
		i += 4
	return array[0]


# part 1
print('part 1:', run(getMem()))

# part 2
for i in range(100):
	for j in range(100):
		array = getMem()
		array[1] = i
		array[2] = j
		if run(array) == 19690720:
			print('Part 2:', 100 * i + j)
			break
		