# 给定一个有序的数组，查找某个数是否在数组中，请编程实现。

def binary_search(s, v):
	left = 0
	right = len(s) - 1

	while left <= right:
		middle = left + int((right - left) / 2)
		if s[middle] > v:
			right = middle - 1
		elif s[middle] < v:
			left = middle + 1
		else:
			return middle
	return -1

if __name__ == '__main__':
	s = [1,2,3,4,5,6,7,8]
	ans = binary_search(s, 7)
	print(ans)
