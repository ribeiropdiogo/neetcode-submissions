class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        res = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                res = i+1
        return res
            






# gas  [1,2,3,4]
# cost [2,2,4,1]


# i----> 0x 1->2->3x 2->3x 3->0->1->2->3 ok
# gas--> 1. 2->3->-1 3->-1 4->5->5->6->3

        