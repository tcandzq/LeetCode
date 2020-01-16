# -*- coding: utf-8 -*-
# @File    : ContainsDuplicateII.py
# @Date    : 2020-01-15
# @Author  : tc
"""
题号 219 存在重复元素II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

参考:https://leetcode-cn.com/problems/contains-duplicate-ii/solution/hua-jie-suan-fa-219-cun-zai-zhong-fu-yuan-su-ii-by/
1.维护一个哈希表，里面始终最多包含 k 个元素，当出现重复值时则说明在 k 距离内存在重复元素
2.每次遍历一个元素则将其加入哈希表中，如果哈希表的大小大于 k，则移除最前面的数字

"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index,num in enumerate(nums):
            if num in d:
                return True
            d[num] = index
            if len(d) > k:
                d.pop(nums[index-k])
        return False



if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums,k))