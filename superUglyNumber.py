#Using generators and heapq.merge. Too bad there's no itertools.unique.
#from Leetcode Discuss

def nthSuperUglyNumber(self, n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]