

a, b = list(map(int, input('type a (a, b) to get sum of it: ').split()))

res = lambda a, b: a if b == 1 else \
		a + calc (a, b-1)

def calc(a, b):
	count  = 0
	while b > 0:
		count += a
		b -= 1
	return count 



print(res(a, b))
