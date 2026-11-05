class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            newVal = digits[i] + 1
            if newVal < 10:
                digits[i] = newVal
                return digits
            else:
                digits[i] = 0
        
        return [1]+digits 