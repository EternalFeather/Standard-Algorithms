# 输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，
# 每个子数组都有一个和。 求所有子数组的和的最大值，要求时间复杂度为O(n)。
# 例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2， 
# 因此输出为该子数组的和18。

def find_max_sum(s):
	num = 0
	total = s[0]
	for i in range(1, len(s)):
		if total <= 0:
			total = s[i]
		else:
			total += s[i]
		if total > num:
			num = total
	return num

if __name__ == '__main__':
	s = [1, -2, 3, 10, -4, 7, 2, -5]
	ans = find_max_sum(s)
	print(ans)