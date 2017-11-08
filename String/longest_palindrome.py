# 给定一个字符串，求它的最长回文子串的长度。

def longestPalindrome(s, n):
	maxnum = 1
	if not s or n < 1:
		return 0
	for i in range(n):
		num = 1
		d = 1
		while i-d>=0 and i+d<n:
			if s[i-d] != s[i+d]:
				break
			else:
				num += 2
				d += 1
		if num > maxnum:
			maxnum = num
	return maxnum

# def Manacher(s, n):
	


if __name__ == '__main__':
	s = "bcabcbcb"
	st = [i for i in s]
	ans1 = longestPalindrome(st, len(st))
	print(ans1)
	# ans2 = Manacher(st, len(st))
	# print(ans2)
