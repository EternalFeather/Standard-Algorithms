# 输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字。
# 要求时间复杂度是O(N)。如果有多对数字的和等于输入的数字，输出任意一对即可。
# 例如输入数组1、2、4、7、11、15和数字15。由于4+11=15，因此输出4和11。

# time:O(N^2) / space:O(1)
def residual(s, k):
	ans = []
	temp = [(k-i) for i in s]
	i, j = 0, len(temp)-1
	for i in s:
		if i in temp:
			if i not in ans:
				ans.append((i, k-i))
	return ans

# time:O(NlogN) / O(1)
def sort(s, k):
	ans = []
	left = 0
	right = len(s)-1
	while left < right:
		num = s[left] + s[right]
		if num == k:
			if num not in ans:
				ans.append((s[left], s[right]))
			right -= 1
			left += 1
		elif num > k:
			right -= 1
		else:
			left += 1
	return ans


if __name__ == '__main__':
	s = [0, 2, 4, 7, 11, 15]
	k = 15
	result1 = residual(s, k)
	print(result1)
	result2 = sort(s, k)
	print(result2)