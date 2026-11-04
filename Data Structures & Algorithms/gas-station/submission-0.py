class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, index = 0, 0
        # Clear the impossible case
        if sum(cost) > sum(gas):
            return -1
        # Iterate gas stations
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                index = (i + 1) % len(gas)
                tank = 0
        return index



        