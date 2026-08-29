class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))
        result = nums[:]

        start = 0

        while start < len(arr):
            end = start

            while end + 1 < len(arr) and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            values = sorted(x[0] for x in arr[start:end + 1])
            indices = sorted(x[1] for x in arr[start:end + 1])

            for i in range(len(values)):
                result[indices[i]] = values[i]

            start = end + 1

        return result