#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 22:11
# @Author  : tc
# @File    : SlidingWindowMaximum.py
"""
题号:239 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

可参考:https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-shu-zu-by-powcai/

本题有多种解答,我是用双端队列求解的时间复杂度是O(n^2)的。先占个坑吧,后面有时间吧动态规划和O(1)的解法补充了

"""
from collections import deque

def maxSlidingWindow(nums,k):
    if not nums:
        return []
    n = len(nums)
    if k == n:
        return [max(nums)]
    d = deque(nums[0:k])
    res = []
    for i in range(n-k+1):
        print(d)
        res.append(max(d))
        d.popleft()
        if i+k >= n:
            break
        d.append(nums[i+k])
    return res

if __name__ == '__main__':
    nums = []
    k = 0
    print(maxSlidingWindow(nums,k))