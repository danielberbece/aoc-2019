def read_input():
	moons = []
	moons.append([3,15,8])
	moons.append([5,-1,-2])
	moons.append([-10,8,2])
	moons.append([8, 4, -5])
	return moons

def read_exinput():
	moons = []
	moons.append([-1,0,2])
	moons.append([2,-10,-7])
	moons.append([4,-8,8])
	moons.append([3,5,-1])
	return moons


def tick(moons_pos, moons_vel):
	# print(moons_pos)
	# print(moons_vel)
	calculate_vel(moons_pos, moons_vel)
	move(moons_pos, moons_vel)

def move(moons_pos, moons_vel):
	for i in range(len(moons_pos)):
		for coord in range(3):
			moons_pos[i][coord] += moons_vel[i][coord]

def calculate_vel(moons_pos, moons_vel):
	for i in range(len(moons_pos)):
		for j in range(i + 1, len(moons_pos)):
			if i != j:
				for x in range(3):
					if moons_pos[i][x] != moons_pos[j][x]:
						increment_vel(moons_vel[i], x, moons_pos[i][x] < moons_pos[j][x])
						increment_vel(moons_vel[j], x, moons_pos[i][x] > moons_pos[j][x])

def increment_vel(moons_vel, coord, inc):
	if inc:
		moons_vel[coord] += 1
	else:
		moons_vel[coord] -= 1

def energy(moons_vel):
	s = 0
	for m in moons_vel:
		s += abs(m)
	return s

def total_energy(moons_pos, moons_vel):
	total = 0
	for i in range(len(moons_pos)):
		total += energy(moons_pos[i]) * energy(moons_vel[i])

	return total

#part 1
moons_pos = read_input()
moons_vel = [[0,0,0] for _ in moons_pos]

for i in range(1000):
	tick(moons_pos, moons_vel)

print("part 1", total_energy(moons_pos, moons_vel))

#part 2
step = 0
moons_pos = read_input()
moons_vel = [[0,0,0] for _ in moons_pos]
states = {(moons_pos[0][3], moons_vel[0][3],
		moons_pos[1][3], moons_vel[1][3],
		moons_pos[2][3], moons_vel[2][3],
		moons_pos[3][3], moons_vel[3][3]): 0}

while True:
	# c_state = (moons_pos[0][0], moons_pos[0][1], moons_pos[0][2], moons_vel[0][0], moons_vel[0][1], moons_vel[0][2])
	tick(moons_pos, moons_vel)
	step += 1
	c_state = (moons_pos[0][3], moons_vel[0][3],
		moons_pos[1][3], moons_vel[1][3],
		moons_pos[2][3], moons_vel[2][3],
		moons_pos[3][3], moons_vel[3][3])
	if c_state in states:
		print(step)
		break
	# else:
	# 	states[c_state] = step
	if step % 1000000 == 0:
		print(step)