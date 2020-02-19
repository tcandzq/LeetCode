# -*- coding: utf-8 -*-
# @File    : FindAllDuplicatesInAnArray.py
# @Date    : 2020-02-19
# @Author  : tc
"""
题号 442 数组中重复的数据
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

参考:https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92390/Python-O(n)-time-O(1)-space

"""
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) -1] *= -1
        return res

if __name__ == '__main__':
    nums =[5,4,6,7,9,3,10,9,5,6]
    solution = Solution()
    print(solution.findDuplicates(nums))

