# 现有n个红白蓝三种不同颜色的小球，乱序排列在一起，
# 请通过两两交换任意两个球，使得从左至右，依次是一些红球、一些白球、一些蓝球。

def swap(s, i, j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp

def Dutch_National_Flag(s):
	begin = 0
	end = len(s) - 1
	if s[begin] == 2 and s[end] == 0:
		swap(s, begin, end)
	while s[begin] == 0:
		begin += 1
	current = begin
	while s[end] == 2:
		end -= 1
	while current <= end:
		if s[current] == 0:
			swap(s, current, begin)
			begin += 1
			current += 1
		elif s[current] == 1:
			current += 1
		else:
			swap(s, current, end)
			current += 1
			end -= 1
 

if __name__ == '__main__':
	s = [2, 0, 2, 1, 1, 2, 0, 1, 1, 1]
	Dutch_National_Flag(s)
	print(s)