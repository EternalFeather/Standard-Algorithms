# 回文，英文palindrome，指一个顺着读和反过来读都一样的字符串，
# 比如madam、我爱我，这样的短句在智力性、趣味性和艺术性上都颇有特色，中国历史上还有很多有趣的回文诗。
# 那么，我们的第一个问题就是：判断一个字串是否是回文？
import math

def two_points(s, n):
	if not s or n < 1:
		return False
	front = 0
	back = n - 1
	while front < back:
		if s[front] != s[back]:
			return False
		else:
			front += 1
			back -= 1
	return True

def middle(s, n):
	if not s or n < 1:
		return False
	if n % 2 == 0:
		left = int(n / 2 - 1)
		right = int(n / 2)
	else:
		left = int(math.floor(n / 2) - 1)
		right = int(math.ceil(n / 2))
	while left >= 0:
		if s[left] != s[right]:
			return False
		else:
			left -= 1
			right += 1
	return True


if __name__ == '__main__':
	s = "abcbcba"
	st = [i for i in s]
	# O(n) / O(1)
	ans1 = two_points(st, len(st))
	print(ans1)
	# O(n) / O(1)
	ans2 = middle(st, len(st))
	print(ans2)
