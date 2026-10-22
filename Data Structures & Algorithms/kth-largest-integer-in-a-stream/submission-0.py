class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        largest = []
        for v in self.nums:
            temp = v
            if largest:
                # Create a list in descending order
                for i in range(len(largest)):
                    if temp > largest[i]:
                        aux = largest[i]
                        largest[i] = temp
                        temp = aux
            largest.append(temp)
        return largest[self.k-1]
        
