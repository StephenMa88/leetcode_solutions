class Solution:
    def fib(self,N: int) -> int:
        # input is which Fib number and output is the value of the Fib in N place
        # lambda is used to create a def without having to actually specify def
        # the input is x and what the def does is explained after the colon
        # if it is less than or equal to 1 it will output 1
        # otherwise it will look for the fib number specified by N 
        ans = lambda x:x if x<=1 else ans(x-1)+ans(x-2)
        return ans(N)
