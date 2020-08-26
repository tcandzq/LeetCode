# -*- coding: utf-8 -*-
# @File    : ConstrainedSubsequenceSum.py
# @Date    : 2020-08-27
# @Author  : tc
"""
题号 1425. 带限制的子序列和
给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。

数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。



示例 1：

输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。
示例 2：

输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。
示例 3：

输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。


提示：

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

参考：https://leetcode.com/problems/constrained-subsequence-sum/discuss/597751/JavaC%2B%2BPython-O(N)-Decreasing-Deque

"""
from typing import List
import collections

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deque = collections.deque()
        for i in range(len(nums)):
            nums[i] += deque[0] if deque else 0
            while len(deque) and nums[i] > deque[-1]:
                deque.pop()
            if nums[i] > 0:
                deque.append(nums[i])
            if i >= k and deque and deque[0] == nums[i - k]:
                deque.popleft()
        return max(nums)


if __name__ == '__main__':
    pass