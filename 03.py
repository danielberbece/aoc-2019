array = []
f = open('03.txt', 'r')
# f = open('ex', 'r')
first_line = f.readline().split(',')
second_line = f.readline().split(',')

m = {}
pos = [0, 0]
steps = 1
for el in first_line:
	if el[0] == 'D':
		for i in range(int(el[1:])):
			pos[1] -= 1
			m[(pos[0], pos[1])] = steps
			steps +=1
	if el[0] == 'R':
		for i in range(int(el[1:])):
			pos[0] += 1
			m[(pos[0], pos[1])] = steps
			steps +=1
	if el[0] == 'U':
		for i in range(int(el[1:])):
			pos[1] += 1
			m[(pos[0], pos[1])] = steps
			steps +=1
	if el[0] == 'L':
		for i in range(int(el[1:])):
			pos[0] -= 1
			m[(pos[0], pos[1])] = steps
			steps +=1
		

closes_distance = 999999999999990909090
pos = [0, 0]
# for el in second_line:
# 	if el[0] == 'D':
# 		for i in range(int(el[1:])):
# 			pos[1] -= 1
# 			if (pos[0], pos[1]) in m and (m[(pos[0], pos[1])] == 1 or m[(pos[0], pos[1])] == 3):
# 				m[(pos[0], pos[1])] = 3
# 				print('Inter')
# 				if  abs(pos[1]) + abs(pos[0])   < closes_distance:
# 					closes_distance =  abs(pos[1]) + abs(pos[0]) 
# 			else:
# 				m[(pos[0], pos[1])] = 2
# 	if el[0] == 'R':
# 		for i in range(int(el[1:])):
# 			pos[0] += 1
# 			if (pos[0], pos[1]) in m and (m[(pos[0], pos[1])] == 1 or m[(pos[0], pos[1])] == 3):
# 				m[(pos[0], pos[1])] = 3
# 				print('Inter')
# 				if  abs(pos[1]) + abs(pos[0])  < closes_distance:
# 					closes_distance =  abs(pos[1]) + abs(pos[0]) 
# 			else:
# 				m[(pos[0], pos[1])] = 2
# 	if el[0] == 'U':
# 		for i in range(int(el[1:])):
# 			pos[1] += 1
# 			if (pos[0], pos[1]) in m and  (m[(pos[0], pos[1])] == 1 or m[(pos[0], pos[1])] == 3):
# 				m[(pos[0], pos[1])] = 3
# 				print('Inter')
# 				if  abs(pos[1]) + abs(pos[0])  < closes_distance:
# 					closes_distance =  abs(pos[1]) + abs(pos[0]) 
# 			else:
# 				m[(pos[0], pos[1])] = 2
# 	if el[0] == 'L':
# 		for i in range(int(el[1:])):
# 			pos[0] -= 1
# 			if (pos[0], pos[1]) in m and (m[(pos[0], pos[1])] == 1 or m[(pos[0], pos[1])] == 3):
# 				m[(pos[0], pos[1])] = 3
# 				print('Inter')
# 				if abs(pos[1]) + abs(pos[0])  < closes_distance:
# 					closes_distance = abs(pos[1]) + abs(pos[0]) 
# 			else:
# 				m[(pos[0], pos[1])] = 2
max_steps = 999999999900
steps = 1
for el in second_line:
	if el[0] == 'D':
		for i in range(int(el[1:])):
			pos[1] -= 1
			if (pos[0], pos[1]) in m and m[(pos[0], pos[1])] + steps < max_steps:
				max_steps = m[(pos[0], pos[1])] + steps
				print(m[(pos[0], pos[1])] ,steps)
			steps += 1
	if el[0] == 'R':
		for i in range(int(el[1:])):
			pos[0] += 1
			if (pos[0], pos[1]) in m and m[(pos[0], pos[1])] + steps < max_steps:
				max_steps = m[(pos[0], pos[1])] + steps
				print(m[(pos[0], pos[1])] ,steps)
			steps += 1
	if el[0] == 'U':
		for i in range(int(el[1:])):
			pos[1] += 1
			if (pos[0], pos[1]) in m and m[(pos[0], pos[1])] + steps < max_steps:
				max_steps = m[(pos[0], pos[1])] + steps
				print(m[(pos[0], pos[1])] ,steps)
			steps += 1
		
	if el[0] == 'L':
		for i in range(int(el[1:])):
			pos[0] -= 1
			if (pos[0], pos[1]) in m and m[(pos[0], pos[1])] + steps < max_steps:
				max_steps = m[(pos[0], pos[1])] + steps
				print(m[(pos[0], pos[1])] ,steps)
			steps += 1
	

print(max_steps)