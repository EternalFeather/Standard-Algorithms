# 给一个浮点数序列，取最大乘积连续子串的值，
# 例如 -2.5，4，0，3，0.5，8，-1，则取出的最大乘积连续子串为3，0.5，8。
# 也就是说，上述数组中，3 0.5 8这3个数的乘积3*0.5*8=12是最大的，而且是连续的。

# Time:O(n^2)
def violate(s):
	maxnum = s[0]
	for i in range(len(s)):
		temp = 1
		for j in range(i, len(s)):
			temp *= s[j]
			if temp > maxnum:
				maxnum = temp
	return maxnum

# Time:O(n)
def dynamic(s):
	maxend = s[0]
	minend = s[0]
	maxnum = s[0]
	for i in range(1, len(s)):
		end1 = maxend * s[i]
		end2 = minend * s[i]
		maxend = max(max(end1, end2), s[i])
		minend = min(min(end1, end2), s[i])
		maxnum = max(maxnum, maxend)
	return maxnum

if __name__ == '__main__':
	s = [-2.5, 4, 0, 3, 0.5, 8, -1]
	ans1 = violate(s)
	print(ans1)
	ans2 = dynamic(s)
	print(ans2)
