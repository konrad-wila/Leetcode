class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set to remove duplicates.
        unique_nums = set(nums)
        # If the length of the set is different from the length of the original list,
        # it means there were duplicates.
        return len(unique_nums) != len(nums)
