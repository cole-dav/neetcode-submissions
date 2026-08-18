class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n==2:
            return 2
        i = 1
        sol = [1,2]
        while i < n:
            sol.append(sol[i] + sol[i-1])
            i+=1
        return sol[n-1]