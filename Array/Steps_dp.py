# 一个台阶总共有n 级，如果一次可以跳1 级，也可以跳2 级。
# 求总共有多少总跳法，并分析算法的时间复杂度。

def Fibonacci(n):
	if n <= 0:
		return
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

if __name__ == '__main__':
	ans = Fibonacci(4)
	print(ans)