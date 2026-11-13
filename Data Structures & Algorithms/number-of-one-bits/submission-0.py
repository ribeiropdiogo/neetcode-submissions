class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = f'{n:08b}'
        res = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                res += 1
        return res