# 数组中有一个数字出现的次数超过了数组长度的一半，找出这个数字。

def FindNumber(s):
	# 前提一定要存在超过半数的条件，否则用hash
	candidate = s[0]
	nTimes = 1
	for i in range(1, len(s)):
		if nTimes == 0:
			candidate = s[i]
			nTimes = 1
		else:
			if s[i] == candidate:
				nTimes += 1
			else:
				nTimes -= 1
	return candidate

if __name__ == '__main__':
	s = [0,1,2,1,1,2,1]
	s2 = [0,1,2,1]
	res = FindNumber(s2)
	print(res)
