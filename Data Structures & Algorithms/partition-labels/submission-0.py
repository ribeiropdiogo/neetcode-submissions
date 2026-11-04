class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
                
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res




        #     0123456789012
        #s = "xyxxyzbzbbisl"

        #x -> 0 2 3 
        #y -> 1 4

        #z -> 5 7
        #b -> 6 8 9

        #i -> 10

        #s -> 11

        #l -> 12