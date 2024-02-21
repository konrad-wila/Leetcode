class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                # Number is duplicate
                return True
            num_set.add(num)
        return False
