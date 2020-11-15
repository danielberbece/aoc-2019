def getInput():
	return list(open('08.in', 'r').read())

width = 25
height = 6

def part1():
	global width, height
	i = 0
	img = getInput()

	zeros = 0
	ones = 0
	twos = 0
	minV = [999999999, 0]
	while i < len(img):
		if i % (width * height) == 0 and i != 0:
			if zeros < minV[0]:
				minV[0] = zeros
				minV[1] = ones * twos
			zeros = 0
			ones = 0
			twos = 0

		if img[i] == '0':
			zeros += 1
		elif img[i] == '1':
			ones += 1
		elif img[i] == '2':
			twos += 1
		i += 1

	if zeros < minV[0]:
		minV[0] = zeros
		minV[1] = ones * twos

	print("part1:",minV[1])


def print_img(img):
	global width, height
	for y in range(height):
		for x in range(width):
			if img[x + y * width] == '1':
				print('#', end = ' ')
			else:
				print(' ', end = ' ')
		print("")

def part2():
	global width, height
	img = getInput()
	final_img = img[:(width * height)]

	i = width * height
	while i < len(img):
		pos = i % (width * height)
		if final_img[pos] == '2':
			final_img[pos] = img[i]
		i += 1

	print_img(final_img)


part1()
part2()