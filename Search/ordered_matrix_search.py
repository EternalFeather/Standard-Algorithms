# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。(杨氏矩阵)
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def search(s, k):
	if not s[0]:
		return False
	row = len(s) - 1
	col = 0
	while row >= 0 and col < len(s[0]):
		temp = s[row][col]
		if temp == k:
			return True
		elif temp > k:
			row -= 1
		else:
			col += 1
	return False


if __name__ == '__main__':
	s = [[1,2,3],
		 [4,5,6],
		 [6,7,8]]
	k = 2
	res = search(s, k)
	print(res)