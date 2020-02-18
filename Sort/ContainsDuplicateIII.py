# -*- coding: utf-8 -*-
# @File    : ContainsDuplicateIII.py
# @Date    : 2020-02-18
# @Author  : tc
"""
220 存在重复元素III
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

桶排序:
用t+1作为桶的容量，动态删除距离大于k的桶元素

代码参考：https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets

思路参考：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/cun-zai-zhong-fu-yuan-su-iii-by-leetcode/

"""
from typing import List

class Solution:
    # 超时
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(1,k+1):
                if i+j < n and abs(nums[i] - nums[i+j]) <= t:
                    return True
        return False

    # 桶排序
    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < w:
                return True
            if m+1 in d and abs(nums[i] - d[m+1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                # 动态删除桶中元素的索引距离大于k的元素，
                # 不用担心后面的元素可能需要这个桶里的元素，因为下一个元素 i+1 肯定与这个删除的桶内元素距离更远
                del d[nums[i-k] // w]
        return False

if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    t = 2

    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate2(nums,k,t))