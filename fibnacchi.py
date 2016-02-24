def fibnacci(N):
	if N == 1:
		return 0
	elif N == 2:
		return 1
	else:
		return fibnacci(N - 1) + fibnacci(N - 2)
print fibnacci(5)