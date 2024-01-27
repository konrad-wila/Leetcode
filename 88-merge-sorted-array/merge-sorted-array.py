class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2, mergeIndex = m - 1, n - 1, m + n - 1

        # Continue until all elements of nums2 are merged
        while index2 >= 0:
            # If nums1 is exhausted or the current element in nums2 is larger
            if index1 < 0 or nums2[index2] >= nums1[index1]:
                nums1[mergeIndex] = nums2[index2]
                index2 -= 1
            else:
                nums1[mergeIndex] = nums1[index1]
                index1 -= 1
            mergeIndex -= 1

    # Direct copying of the remaining elements of nums2, if any
        if index2 >= 0:
            nums1[: index2 + 1] = nums2[: index2 + 1]
