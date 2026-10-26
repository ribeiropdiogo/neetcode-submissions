class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, comb = [], []
        letterMap = {"2": 97, "3": 100, "4": 103, "5": 106, "6": 109, "7": 112, "8": 116, "9": 119}
        def combinations(d):
            if d > len(digits) or len(digits) == 0:
                return
            if d == len(digits):
                res.append("".join(comb))
                return
            if int(digits[d]) in [2,3,4,5,6,8]:
                l = 3
            elif int(digits[d]) in [7,9]:
                l = 4
            for i in range(l):
                comb.append(chr(letterMap[digits[d]]+ i))
                combinations(d+1)
                comb.pop()

        combinations(0)

        return res
