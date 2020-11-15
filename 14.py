def get_input():
	rows = open('14.in', 'r').read().split('\n')
	reactions = [x.split('=>') for x in rows]
	b_react = [[x[1], *x[0].split(',')] for x in reactions]
	z =  [b_react[0], *b_react[1:]]
	r = []
	for x in z:
		tmp = []
		for a in x:
			val = a.strip().split(' ')
			tmp.append([int(val[0]), val[1]])
		r.append(tmp)
	return r


def make_react_table(all_r):
	mm = {}
	for reaction in all_r:
		mm[reaction[0][1]] = [reaction[0][0], *reaction[1:]]
	return mm

def make_stash(r_table):
	global INIT_ORE
	stash = {}
	for elem in r_table:
		stash[elem] = 0
	stash['ORE'] = INIT_ORE
	return stash

def make_fuel(r_table, stash):
	Q = [[1, 'FUEL']]
	ores = 0
	while len(Q) != 0:
		pair = Q.pop(0)
		if pair[1] == 'ORE':
			ores += pair[0]
		else:
			while stash[pair[1]] < pair[0] and pair[0] > 0:
				pair[0] -= r_table[pair[1]][0]
				for x in r_table[pair[1]][1:]:
					Q.append(x.copy())
			if pair[0] != 0:
				stash[pair[1]] = stash[pair[1]] + (- pair[0])
	return ores

def make_fuel2(r_table, stash):
	ores = 0
	quantity = 1
	while True:
		Q = [[1000, 'FUEL']]
		ores_tmp = 0
		while len(Q) != 0:
			pair = Q.pop(0)
			if pair[1] == 'ORE':
				ores_tmp += pair[0]

			else:
				while stash[pair[1]] < pair[0] and pair[0] > 0:
					pair[0] -= r_table[pair[1]][0]
					for x in r_table[pair[1]][1:]:
						Q.append(x[:])
						# print(x)
				if pair[0] != 0:
					stash[pair[1]] = stash[pair[1]] + (- pair[0])
		if ores + ores_tmp > 1000000000000:
			print(ores)
			break
		else:
			ores += ores_tmp
			print(ores)

def get_res(pair):
	global r_table, stash, ores
	# print(pair, stash)
	if pair[1] == 'ORE':
		ores += pair[0]
	else:
		cpy_pair = pair[0]
		if pair[0] <= stash[pair[1]]:
			stash[pair[1]] = stash[pair[1]] - pair[0]
		else:
			need = pair[0] - stash[pair[1]]
			freq = need // r_table[pair[1]][0]
			if (freq * r_table[pair[1]][0] < need):
				freq += 1
			for x in r_table[pair[1]][1:]:
				get_res([x[0] * freq, x[1]])
			stash[pair[1]] = freq * r_table[pair[1]][0] - need

def search(interval):
	global ores, r_table, stash
	if interval[0] >= interval[1]:
		return -1
	mid = (interval[0] + interval[1]) // 2
	ores = 0
	stash = make_stash(r_table)
	get_res([mid, 'FUEL'])
	cp_ores = ores
	ores = 0
	stash = make_stash(r_table)
	get_res([mid + 1, 'FUEL'])
	
	if cp_ores < 1000000000000 and ores > 1000000000000:
		return mid
	elif ores < 1000000000000:
		return search([mid + 1, interval[1]])
	elif cp_ores > 1000000000000:
		return search([interval[0], mid])


INIT_ORE = 0
r_table = make_react_table(get_input())
stash = make_stash(r_table)

print("part1:", make_fuel(r_table, stash))

interval = [1, 2149000000]
ores = 0
print('part2:', search(interval))