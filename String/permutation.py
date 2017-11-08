# 输入一个字符串，打印出该字符串中字符的所有排列。
# 例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串
# abc、acb、bac、bca、cab 和 cba。

def swap(perm, i, j):
	temp = perm[i]
	perm[i] = perm[j]
	perm[j] = temp


def recursive(perm, first, last):
	global count
	if not perm or last < 1:
		return
	if first == last:
		count += 1
		print(perm)
	else:
		for i in range(first, last):
			if not_equal(perm, first, i):
				swap(perm, i, first)
				recursive(perm, first + 1, last)
				swap(perm, i, first)


def perm(result, perms, size, respos):
	global count1
	if not perms or size < 1:
		return
	if respos == size:
		count1 += 1
		print(result)
	else:
		for i in range(size):
			if not_equal(perms, 0, i):
				result.append(perms[i])
				perm(result, perms, size, respos+1)
				result.pop()


def not_equal(s, i, j):
	for k in range(i, j):
		if s[k] == s[j]:
			return False
	return True


def subset(s, n):
	k = 0
	lis = [0 for _ in range(n+1)]
	while True:
		if lis[k] < n:
			lis[k+1] = lis[k] + 1
			k += 1
		else:
			lis[k-1] += 1
			k -= 1
		if k == 0:
			break
		print("{", ",".join(s[lis[i] - 1] for i in range(1, k+1)), "}")	


if __name__ == '__main__':
	s = "123"
	count = 0
	count1 = 0
	st = [i for i in s]
	# O(n!)
	ans = []
	recursive(st, 0, len(st))
	print(count)
	temp = []
	perm(temp, st, len(st), 0)
	print(count1)
	subset(st, len(st))
