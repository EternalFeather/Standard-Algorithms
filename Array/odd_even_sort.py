# 输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，
# 所有偶数位于数组的后半部分。要求时间复杂度为O(n)。

# 保证奇数和奇数，偶数和偶数之间的相对位置不变
def odd_even_sort(s):
	ans = []
	if len(s) == 0:
		return []
	temp = 0
	for i in s:
		if i % 2 == 0:
			ans.append(i)
		else:
			ans.insert(temp, i)
			temp += 1
	return ans


def swap(s, i, j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp


# 不用保证先后位置，time : O(N)
def point(s):
	if len(s) == 0:
		return []
	point1 = 0
	for point2 in range(len(s)-1):
		if s[point2 + 1] % 2 != 0:
			point1 += 1
			swap(s, point1, point2 + 1)
	return s


if __name__ == '__main__':
	# [1,3,5,7,9,4,6,2,8]
	s = [1,3,4,6,2,5,8,7,9]
	ans1 = odd_even_sort(s)
	print(ans1)
	ans2 = point(s)
	print(ans2)
