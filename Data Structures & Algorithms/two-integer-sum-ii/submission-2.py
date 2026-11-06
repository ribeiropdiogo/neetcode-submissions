class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
    
    # numbers -> increasing order
    # numbers = [1,2,3,4]
    # target = 7
    # [1,2,3,4]
    #  i     j