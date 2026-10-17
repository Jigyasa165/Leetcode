
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findPosition(first):
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid

                    if first:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        first = findPosition(True)
        last = findPosition(False)

        return [first, last]
