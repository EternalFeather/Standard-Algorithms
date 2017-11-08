# 给定一个源串和目标串，能够对源串进行如下操作：
# 1、在给定位置上插入一个字符
# 2、替换任意字符
# 3、删除任意字符
# 写一个程序，返回最小操作数，使得对源串进行这些操作后等于目标串，源串和目标串的长度都小于2000。

# dp[i][j] =min{
# 	dp[i-1][j] + 1  	  S[i]不在T[0…j]中
# 	dp[i-1][j-1] + 1/0    S[i]在T[j]
# 	dp[i][j-1] + 1  	  S[i]在T[0…j-1]中

def dynamic_programing(s, t):
	s_ = [i for i in s]
	t_ = [i for i in t]
	dp = [[0 for _ in range(len(t_)+1)] for _ in range(len(s_)+1)]
	# boundary condition : s or t == None
	for i in range(1, len(s_)+1):
		dp[i][0] = i
	for j in range(1, len(t_)+1):
		dp[0][j] = j
	for i in range(1, len(s_)+1):
		for j in range(1, len(t_)+1):
			temp = min(dp[i-1][j]+1, dp[i][j-1]+1)
			d = 0
			if s_[i - 1] == t_[j - 1]:
				d = 0
			else:
				d = 1
			dp[i][j] = min(temp, dp[i-1][j-1]+d)
	res = dp[len(s_)][len(t_)]
	print(dp)
	for i in range(len(s_)):
		for j in range(len(t_)):
			dp[i][j] == None
	return res

if __name__ == '__main__':
	# s : A L G O R   I   T H M
	# t : A L   T R U I S T I C
	# 最后一个可能情况1、字符-空白 2、空白-字符 3、字符-字符 4、空白-空白(No)
	# condition1 : 删除字符(dp[i-1][j] + 1)
	# condition2 : 添加字符(dp[i][j-1] + 1)
	# condition3 : 修改字符(dp[i-1][j-1] + (s[i] == t[j] ? 0 : 1))
	# dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(s[i]==t[j]?0:1))

	s = "ALGORITHM"
	t = "ALTRUISTIC"
	ans = dynamic_programing(s, t)
	print(ans)