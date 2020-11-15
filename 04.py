start = '248345'
finish = '746315'
cnt = 0

def hasDouble(num):
	for i in range(len(num) - 1):
		if num[i] == num[i + 1]:
			return True
	return False

def hasOnlyDouble(num):
	ans = False
	if num[0] == num[1] and num[1] != num[2]:
		ans = True
	for i in range(1, len(num) - 2):
		if num[i] != num[i - 1] and num[i] == num[i + 1] and num[i] != num[i + 2]:
			ans = True
	if num[-1] == num[-2] and num[-2] != num[-3]:
		ans = True
	return ans

def isIncreasing(num):
	for i in range(len(num) - 1):
		if int(num[i]) > int(num[i + 1]):
			return False
	return True

def inRange(num):
	global start, finish
	if int(start) <= int(num) and int(num) <= int(finish):
		return True
	return False

def back(k, num):
	global finish, cnt
	if k == 6:
		if hasDouble("".join(num)) and isIncreasing("".join(num)) and inRange("".join(num)):
			cnt += 1
	else:
		for i in range(10):
			num[k] = str(i)
			back(k + 1, num)

def back2(k, num):
	global finish, cnt
	if k == 6:
		if hasOnlyDouble("".join(num)) and isIncreasing("".join(num)) and inRange("".join(num)):
			cnt += 1
	else:
		for i in range(10):
			num[k] = str(i)
			back2(k + 1, num)

back(0, list("000000"))
print("Part 1:",cnt)
cnt = 0
back2(0, list("000000"))
print("Part 2:",cnt)

