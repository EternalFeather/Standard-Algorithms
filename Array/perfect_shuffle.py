# 有个长度为2n的数组{a1,a2,a3,...,an,b1,b2,b3,...,bn}，
# 希望排序后{a1,b1,a2,b2,....,an,bn}，请考虑有无时间复杂度o(n)，空间复杂度0(1)的解法。
# 看似简单，按照题目所要排序后的字符串蛮力变化即可，
# 但若要完美的达到题目所要求的时空复杂度，则需要我们花费不小的精力。

def swap(s, i, j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp

# time : O(N^2)
def step_by_step(s):
	first = 0
	end = int(len(s) / 2)
	cur = end
	while end < len(s):
		first += 1
		while cur > first:
			swap(s, cur, cur - 1)
			cur = cur - 1
		first += 1
		end += 1
		cur = end
	return s

# swap in place : i -> (2*i) % (2*n+1)
# cycle_leader
# 2*n = 3^k-1

if __name__ == '__main__':
	s = [1,1,1,1,2,2,2,2]
	ans = step_by_step(s)
	print(ans)