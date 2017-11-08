# 有n*n个格子，每个格子里有正数或者0，从最左上角往最右下角走，
# 只能向下和向右，一共走两次（即从左上角走到右下角走两趟），
# 把所有经过的格子的数加起来，求最大值SUM，且两次如果经过同一个格子，
# 则最后总和SUM中该格子的计数只加一次。

def IsValid(step, x1, x2, n):
	y1 = step - x1
	y2 = step - x2
	return x1 >= 0 and x1 < n and x2 >= 0 and x2 < n and y1 >= 0 and y1 < n and y2 >= 0 and y2 < n

def GetValue(step, x1, x2, n):
	return dp[step][x1][x2] if IsValid(step, x1, x2, n) else -inf

# O(n^3)
def func1(s, n):
	P = n * 2 - 2
	for i in range(n):
		for j in range(i, n):
			dp[0][i][j] = -inf
	dp[0][0][0] = s[0][0]
	for step in range(1, P+1):
		for i in range(n):
			for j in range(i, n):
				dp[step][i][j] = -inf
				if (not IsValid(step, i, j, n)):
					continue
				if i != j:
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i-1, j-1, n))
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i-1, j, n))
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i, j-1, n))
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i, j, n))
					dp[step][i][j] += s[i][step-i] + s[j][step-j]
				else:
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i-1, j-1, n))
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i, j-1, n))
					dp[step][i][j] = max(dp[step][i][j], GetValue(step-1, i, j, n))
					dp[step][i][j] += s[i][step-i]
	return dp[P][n-1][n-1]

if __name__ == '__main__':
	N = 202
	inf = 1000000000
	dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N * 2)]
	# s = [[0,0,0,0,0,0,0,0],
	# 	 [0,0,13,0,0,6,0,0],
	# 	 [0,0,0,0,7,0,0,0],
	# 	 [0,0,0,14,0,0,0,0],
	# 	 [0,21,0,0,0,4,0,0],
	# 	 [0,0,15,0,0,0,0,0],
	# 	 [0,14,0,0,0,0,0,0],
	# 	 [0,0,0,0,0,0,0,0]]
	s = [[2,0,8,0,2],
		 [0,0,0,0,0],
		 [0,3,2,0,0],
		 [0,0,0,0,0],
		 [2,0,8,0,2]]
	ans = func1(s, 5)
	print(ans)

