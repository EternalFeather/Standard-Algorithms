# 输入n个整数，输出其中最小的k个。

def swap(s, i, j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp


def bubble_sort(s, first, end):
	flag = True
	i, j = first, 0
	while i < end and flag:
		flag = False
		for j in range(end-i):
			if s[j+1] < s[j]:
				swap(s, j+1, j)
				flag = True
		i += 1


def partitionModify(s, left, right, x):
	i, j = left, right
	while i < j:
		if s[i] >= x:
			while i < j and s[j] >= x:
				j -= 1
			if i != j:
				swap(s, i, j)
				j -= 1
			else:
				break
		i += 1
	if s[i] >= x and i > left:
		return i-1
	return i


def QuickSelect(s, k, left, right):
	if right-left+1<=5:
		bubble_sort(s, left, right)
		return s[left+k-1]
	# 开头n个数都是中位数（5个数一组取中位数）
	for i in range(int((right-left+1)/5)):
		n = left+5*i
		t = n+4
		bubble_sort(s, n, t)
		swap(s, left+i, n+2)
	x = QuickSelect(s, int(((right-left+6)/10)), left, left+int((right-left+1)/5)-1)
	j = partitionModify(s, left, right, x)
	m = j-left+1
	if k <= m:
		return QuickSelect(s, k, left, j)
	else:
		return QuickSelect(s, k-m, j+1, right)
	

if __name__ == '__main__':
	a = [0, 5, 1, 4, 4, 4, 4, 3, 2]
	k = 6
	print(QuickSelect(a, k, 0, len(a)-1))
	# print(",".join(str(a[i]) for i in range(k)))
	print(a)

