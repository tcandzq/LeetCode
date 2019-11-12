#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 21:46
# @Author  : tc
# @File    : CountOfSmallerNumbersAfterSelf.py
"""
题号 315 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

二分查找:有序数组中新插入数字所在的索引等于该数组有多少个数字比新插入数字小
参考1:https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/315-by-ikaruga/
参考2:https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/duo-chong-fang-fa-by-powcai/

"""
from typing import List

class Solution:
    # 二分查找解法
    def countSmaller(self, nums: List[int]) -> List[int]:
        import bisect
        queue = []
        res = []
        print(nums[::-1])
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)  # 二分查找有序数组中num所在的索引
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]





if __name__ == '__main__':
    nums = [5,2,6,1]
    solution = Solution()
    print(solution.countSmaller(nums))