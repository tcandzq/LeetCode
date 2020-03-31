# -*- coding: utf-8 -*-
# @File    : ReorderArray.py
# @Date    : 2020-03-30
# @Author  : tc
"""
面试题21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 != 0:
                left += 1
            print(left)
            while left < right and nums[right] % 2 == 0:
                right -= 1
            if left < right:
                nums[left],nums[right] = nums[right],nums[left]
        return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.exchange(nums))
