# 请编程实现矩阵乘法，并考虑当矩阵规模较大时的优化方法。

# time : O(N^3)
def violate(m1, m2):
	# 4*4
	ans = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m1[0])):
				ans[i][j] += m1[i][k] * m2[k][j]
	return ans


if __name__ == '__main__':
	# 4*3
	m1 = [[1,2,3],[1,2,3],[3,2,1],[3,2,1]]
	# 3*4
	m2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
	result = violate(m1, m2)
	print(result)
