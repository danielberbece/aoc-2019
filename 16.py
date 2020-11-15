import numpy as np

def get_input(repeated=1):
	n = open('16.in', 'r').read()
	initial = [int(x) for x in n]
	if repeated <= 1:
		return initial 
	else:
		return np.tile(initial, repeated)


def create_pattern(i, pattern):
	return np.repeat(pattern, i)


def next_signal(step, signal):
	p_len = step + 1
	mult = 1
	new_signal = 0
	i = p_len - 1
	cnt = 1
	while i < len(signal):
		if mult > 0:
			new_signal += signal[i]
		else:
			new_signal -= signal[i]
		if cnt == p_len:
			i += p_len + 1
			cnt = 1
			mult = 1 - mult
		else:
			cnt += 1
			i += 1
	return abs(new_signal) % 10

def part1():
	signal = get_input()
	pattern = [0, 1, 0, -1]
	phase_patterns = []
	for i in range(1, len(signal) + 1):
		phase_patterns.append(create_pattern(i, pattern))

	n = 100
	for _ in range(n):
		for i in range(len(signal)): 
			signal[i] = next_signal(i, signal, phase_patterns[i])

	print(signal[:8])

def part2():
	signal = get_input(10000)
	tmp = []
	for elem in signal[:7]:
		tmp.append(str(elem))
	offset = int("".join(tmp))
	print(offset, len(signal))

	n = 100
	for p in range(n):
		print(p)
		for i in range(len(signal) - 1, offset - 1, -1):
			signal[i - 1] = (signal[i] + signal[i - 1]) % 10

	print(signal[:8])
	print(signal[offset:offset + 8])


# part1()
part2()