# Longest Common Subsequence
# state : 1->left+up; 2->left; 3->up
def LCSLength(x, y, m, n):
	temp = [[0 for _ in range(n+1)] for _ in range(m+1)]
	state = [[0 for _ in range(n+1)] for _ in range(m+1)]
	# print(temp)
	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1] == y[j-1]:
				temp[i][j] = temp[i-1][j-1] + 1
				state[i][j] = 1
			elif temp[i-1][j] > temp[i][j-1]:
				temp[i][j] = temp[i-1][j]
				state[i][j] = 3
			elif temp[i-1][j] < temp[i][j-1]:
				temp[i][j] = temp[i][j-1]
				state[i][j] = 2
	return state

def LCSPrint(x, m, n, s, ans):
	if m == 0 or n == 0:
		return
	if s[m][n] == 1:
		LCSPrint(x, m-1, n-1, s, ans)
		ans.append(x[m-1])
	elif s[m][n] == 2:
		LCSPrint(x, m, n-1, s, ans)
	else:
		LCSPrint(x, m-1, n, s, ans)
	return ans


if __name__ == '__main__':
	x = "ABCBDAB"
	y = "BDCABA"
	x = [i for i in x]
	y = [i for i in y]
	m = len(x)
	n = len(y)

	ans = []
	state = LCSLength(x, y, m, n)
	LCSPrint(x, m, n, state, ans)
	print("".join(ans))