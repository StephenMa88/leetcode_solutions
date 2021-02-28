class Solution:
    def fib(self,N: int) -> int:
        ans = lambda x:x if x<=1 else ans(x-1)+ans(x-1)
        return ans(N)
