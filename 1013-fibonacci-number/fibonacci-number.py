class Solution:
    def fib(self, n: int) -> int:
        cache = {0: 0, 1: 1}

        def f(n):
            if n in cache:
                return cache[n]
                
            cache[n] = f(n-1) + f(n-2)
            return cache[n]

        return f(n)