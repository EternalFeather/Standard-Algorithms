# 输入三个字符串s1、s2和s3，判断第三个字符串s3是否由前两个字符串s1和s2交错而成，
# 即不改变s1和s2中各个字符原有的相对顺序，
# 例如当s1 = “aabcc”，s2 = “dbbca”，s3 = “aadbbcbcac”时，则输出true，
# 但如果s3=“accabdbbca”，则输出false。

def cross_string(s1, s2, s3):
	s1_, s2_, s3_ = len(s1), len(s2), len(s3)
	if s1_ + s2_ != s3_:
		return False
	dp = [[False for _ in range(s2_+1)] for _ in range(s1_+1)]
	dp[0][0] = True
	for i in range(s1_+1):
		for j in range(s2_+1):
			if dp[i][j] or (i-1>=0 and dp[i-1][j] == True and s1[i-1] == s3[i+j-1]) \
			or (j-1>=0 and dp[i][j-1] == True and s2[j-1] == s3[i+j-1]):
				dp[i][j] = True
			else:
				dp[i][j] = False
	return dp[s1_][s2_]

if __name__ == '__main__':
	s1 = "aabcc"
	s2 = "dbbca"
	s3 = "aadbbcbcac"
	s1_ = [i for i in s1]
	s2_ = [i for i in s2]
	s3_ = [i for i in s3]
	ans = cross_string(s1_, s2_, s3_)
	print(ans)