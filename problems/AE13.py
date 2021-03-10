# Nth Fibbonacci

# O(n)

def getNthFib(n):
    fib = {0: 0, 1: 1}
	for i in range(2, n):
		fib[i] = fib[i-1] + fib[i-2]
		del fib[i-2]
	return fib[n-1]