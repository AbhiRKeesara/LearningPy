# link - https://leetcode.com/problems/concatenation-of-array/
from typing import List


class Solution:
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * (len(nums)))
        for num in range(len(nums)):
            index_for_new_element = num + len(nums)
            ans[num] = nums[num]
            ans[index_for_new_element] = nums[num]
        return ans

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums + nums


sol = Solution()

print(sol.getConcatenation1([1, 2, 1]))
print(sol.getConcatenation2([1, 2, 1]))
