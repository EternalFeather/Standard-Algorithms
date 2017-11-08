# 给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，
# 如把字符串“abcdef”前面的2个字符'a'和'b'移动到字符串的尾部，
# 使得原字符串变成字符串“cdefab”。
# 请写一个函数完成此功能，要求对长度为n的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。
import copy

def violence(s, n):
	temp = s[0];
	for i in range(1, n):
		s[i-1] = s[i]
	s[n-1] = temp

def violence_total(s, n, m):
	while m > 0:
		violence(s, n)
		m -= 1

# ---------------------
#
# ---------------------

def ReverseString(s, left, right):
	while left < right:
		temp = s[left]
		s[left] = s[right]
		s[right] = temp
		left += 1
		right -= 1

def new_func(s, n, m):
	m = m % n
	ReverseString(s, 0, m - 1)
	ReverseString(s, m, n - 1)
	ReverseString(s, 0, n - 1)


if __name__ == '__main__':
	s = "abcdef"
	m = 2
	s = [i for i in s]
	lis1 = copy.deepcopy(s)
	lis2 = copy.deepcopy(s)
	# O(m*n)  O(1)
	violence_total(lis1, len(lis1), m)
	print("".join(lis1))
	# O(n)  O(1)
	new_func(lis2, len(lis2), m)
	print("".join(lis2))