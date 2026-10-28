class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            prevOne = one
            one = one + two
            two = prevOne

        return one