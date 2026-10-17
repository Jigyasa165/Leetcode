
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by the number itself
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its correct sorted index
        index = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or index[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
  