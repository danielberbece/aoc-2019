
def getMem():
	f = open('07.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array

def run(array, inputs):
	in_pos = 0
	i = 0
	while True:
		# take instruction
		if array[i] % 100 == 1:
			#add

			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2 = array[array[i + 2]]

			array[array[i + 3]] = p1 + p2
			i += 4
		elif array[i] % 100 == 2:	 # multiply
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]

			array[array[i + 3]] = p1 * p2
			i += 4
		elif array[i] % 100 == 3:
			array[array[i + 1]] = inputs[in_pos]
			in_pos += 1
			i += 2
		elif array[i] % 100 == 4:
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			# print("ouput:", p1)
			if in_pos == len(inputs):
				return p1
			i += 2
		elif array[i] % 100 == 5:	# jump if true
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			if p1 != 0:
				i = p2
			else:
				i += 3
		elif array[i] % 100 == 6:	# jump if false
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			if p1 == 0:
				i = p2
			else:
				i += 3			
		elif array[i] % 100 == 7:	# less than
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			store_val = 0
			if p1 < p2:
				store_val = 1
	
			array[array[i + 3]] = store_val
			i += 4			
		elif array[i] % 100 == 8:	# eq
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			store_val = 0
			if p1 == p2:
				store_val = 1
	
			array[array[i + 3]] = store_val
			i += 4			
		elif array[i] == 99:
			break
		else:
			print('Wrong instruction', array[i], i)
			exit(-1)
		
	return -1

max_thurst = 0

def runSeq(seq):
	global max_thurst
	prev = 0
	for i in seq:
		# print(i, prev)
		prev = run(getMem(), [i, prev])
	if prev > max_thurst:
		max_thurst = prev

def runSeqLoop(seq):
	global max_thurst
	prevs = [[0],[],[],[],[]]
	halted = [False,False,False,False,False]
	DO = True
	while DO:
		for i in range(len(seq)):
			ret = run(getMem(), [seq[i], *prevs[i]])
			if ret == -1:
				halted[i] = True
				# print(halted, i)
				DO = not(halted[0] and halted[1] and halted[2] and halted[3] and halted[4])
				# if not DO:
				# 	break
				prevs[(i + 1) % 5].append(prevs[i][-1])
			else:
				prevs[(i + 1) % 5].append(ret)
		# print(prevs)
	if prevs[-1][-1] > max_thurst:
		max_thurst = prevs[-1][-1]
		print(seq, prevs[-1])

def back(k, seq, r, method):
	if k == 5:
		method(seq)
	else:
		for i in range(r[0], r[1]):
			if i not in seq:
				seq.append(i)
				back(k + 1, seq, r, method)
				del seq[-1]


# part 1
back(0, [], [0,5], runSeq)
print('part 1:', max_thurst)
# part 2
max_thurst = 0
back(0, [], [5,10], runSeqLoop)
# print('part 2', run(getMem(), [5, 0]))
