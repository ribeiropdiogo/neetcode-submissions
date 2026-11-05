class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            strN = list(str(n))
            sumN = 0
            for i in range(len(strN)):
                sumN += int(strN[i]) * int(strN[i])
            if sumN == 1:
                return True
            elif sumN in seen:
                return False
            else:
                seen.add(sumN)
                n = sumN
