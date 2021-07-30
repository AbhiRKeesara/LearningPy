# link - https://leetcode.com/problems/build-array-from-permutation/

from typing import List

# solution 1:
class Solution:
    def buildArray1(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]

    # solution-2:
    def buildArray2(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


nums = [0, 2, 1, 5, 3, 4]
sol = Solution()
print(sol.buildArray1(nums))
print(sol.buildArray2(nums))
