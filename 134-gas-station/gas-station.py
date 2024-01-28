class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy problem
        # Empty gas tank starting at any station that allows to travel the whole route

        # Chack a solution exists
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        result = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                result = i + 1
        
        return result
