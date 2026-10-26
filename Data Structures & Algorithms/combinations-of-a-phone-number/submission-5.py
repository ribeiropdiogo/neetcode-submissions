class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def combinations(d, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for c in letterMap[digits[d]]:
                combinations(d+1, comb+c)
        
        if digits:
            combinations(0,"")

        return res
