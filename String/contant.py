# 给定两个分别由字母组成的字符串A和字符串B，字符串B的长度比字符串A短。
# 请问，如何最快地判断字符串B中所有字母是否都在字符串A里？
# 为了简单起见，我们规定输入的字符串只包含大写英文字母，
# 请实现函数bool StringContains(string &A, string &B)
# 比如，如果是下面两个字符串：
# String 1：ABCD
# String 2：BAD
# 答案是true，即String2里的字母在String1里也都有，或者说String2是String1的真子集。
# 如果是下面两个字符串：
# String 1：ABCD
# String 2：BCE
# 答案是false，因为字符串String2里的E字母不在字符串String1里。
# 同时，如果string1：ABCD，string 2：AA，同样返回true。

def violence(s1, s2):
	for i in range(len(s2)):
		j = 0
		while j < len(s1) and s1[j] != s2[i]:
			j += 1
		if j == len(s1):
			return False
	return True

def qsort(s1, s2):
	sorted(s1)
	sorted(s2)
	p1, p2 = 0, 0
	while p2 < len(s2):
		while p1 < len(s1) and s1[p1] < s2[p2]:
			p1 += 1
		if p1 == len(s1) or s1[p1] > s2[p2]:
			return False
		p2 += 1
	return True

def multi(s1, s2):
	s1 = list(set(s1))
	s2 = list(set(s2))
	# lis = [2, 3, 5, 6, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
	lis = {'A':2, 'B':3, 'C':5, 'D':7, 'E':11}
	ans = 1
	for i in range(len(s1)):
		ans *= lis[s1[i]]
	for i in range(len(s2)):
		if ans % (lis[s2[i]]) != 0:
			return False
	return True

# ---------------------
#
# ---------------------

def hashed(s1, s2):
	p1 = []
	for i in s1:
		p1.append(hash(i))
	for i in s2:
		if hash(i) not in p1:
			return False
	return True


if __name__ == '__main__':
	s1 = ['A', 'B', 'C', 'D']
	s2 = ['B', 'C', 'E']
	# O(n*m)
	ans1 = violence(s1, s2)
	print(ans1)
	# O(mlogm+nlogn+m+n)
	ans2 = qsort(s1, s2)
	print(ans2)
	# O(m+n)
	ans3 = multi(s1, s2)
	print(ans3)
	# O(m+n)
	ans4 = hashed(s1, s2)
	print(ans4)