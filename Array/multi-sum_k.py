# 输入两个整数n和sum，从数列1，2，3.......n 中随意取几个数，
# 使其和等于sum，要求将其中所有的可能组合列出来。

def Sumofknumber(s, temp, num, n):
	if n < 0 or num <= 0:
		return
	temp.append(s[n])
	if num == s[n]:
		print(temp)
	Sumofknumber(s, temp, num-s[n], n-1)
	temp.pop()
	Sumofknumber(s, temp, num, n-1)


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5, 6, 7]
	k = 6
	temp = []
	Sumofknumber(a, temp, k, len(a)-1)

