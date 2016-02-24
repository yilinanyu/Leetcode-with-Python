def fibnacci(N):
	if N == 1:
		return 0
	elif N == 2:
		return 1
	f0 = 0
	f1 = 1
	f = 0
	i = 3
	while i <= N:
		f = f0 + f1
		f0 = f1
		f1 = f
		i += 1
	return f


