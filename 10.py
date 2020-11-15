import operator, math
def get_input():
	lines = open("ex.in", "r").read().split("\n")
	mm = {}
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == "#":
				mm[(j, i)] = 0

	return mm


def los(point, asteroids):
	point_sight = {}
	for a in asteroids.keys():
		if a != point:
			dx, dy = (a[0] - point[0]), (a[1] - point[1])
			t = math.atan2(dy, dx)
			if t in point_sight:
				point_sight[t].append((-dy, dx))
			else:
				point_sight[t] = [(-dy, dx)]
				
	asteroids[point] = len(point_sight)
	return point_sight

asteroids = get_input()

for a in asteroids:
	los(a, asteroids)

#part 1
elem = max(asteroids.items(), key=operator.itemgetter(1))[0]
print(elem, asteroids[elem])

#part 2
sight = los(elem, asteroids)
cnt = 0
keys_ = sorted(sight.keys(), reverse=True)

for i in keys_:
	if i <= math.pi / 2.0:
		break
	else:
		cnt += 1

keys_ = keys_[cnt:] + keys_[:cnt]
for i in range(200):
	sight[keys_[i % len(keys_)]] = sorted(sight[keys_[i % len(keys_)]], reverse=)
	print(sight[keys_[i % len(keys_)]])
	ast = sight[keys_[i % len(keys_)]].pop(0)
	print(i, -ast[1] + elem[0], - ast[0] + elem[1])

