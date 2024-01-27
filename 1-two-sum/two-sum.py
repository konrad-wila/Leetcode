class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to hold the value and its index
        num_map = {}
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement by subtracting the current number from the target
            complement = target - num
            # Check if the complement is in the dictionary
            if complement in num_map:
                # If found, return the current index and the index of the complement
                return [num_map[complement], i]
            # If not found, add the current number and its index to the dictionary
            num_map[num] = i
        # If no solution is found, return an empty list (or an error message)
        return []