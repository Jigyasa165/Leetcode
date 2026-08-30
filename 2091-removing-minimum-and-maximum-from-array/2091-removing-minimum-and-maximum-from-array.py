class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        option1 = right + 1
        option2 = n - left
        option3 = left + 1 + n - right

        return min(option1, option2, option3)
        