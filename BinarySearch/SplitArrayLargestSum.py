#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 23:05
# @Author  : tc
# @File    : SplitArrayLargestSum.py
"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
注意:
数组长度 n 满足以下条件:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

本题从动态规划移到了二分查找,因为用二分来做真的太巧妙了,而且这种二分解题已经形成了一种套路了,参考leetcode
二分查找:看了很久才明白一点点,这里面其实有一个原则,就是一个数组被切分的次数越多,那么各个数组的和的最大值会越小。
由于切分后数组和的范围必定在[max(nums),sum(nums)]。注意这里是用一个[max(nums),sum(nums)]来逼近切分数组后的最大值。

参考1:https://github.com/grandyang/leetcode/issues/410
参考2:https://leetcode-cn.com/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-coder233-2/

"""
# 二分解法
def splitArray(nums,m):
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if can_split(nums, m, mid):
            right = mid  # 如果当前的mid使得用小于给定的m次切分完,说明mid太大了;
        else:
            left = mid + 1  # 如果当前的mid使得切分的次数超过了m,因为说明mid太大了;
    return right

def can_split(nums,m,sum):
    cnt = 1
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum > sum:  # 如果当前切分的数组和大于mid
            cur_sum = nums[i]  # 表示1次切分已经结束了,cur_sum 清空后重新初始化,其实就是使得切分后的数组和要不大于mid
            cnt += 1  # 切分次数+1,
            if cnt > m:  # 如果切分次数超过了m,
                return False
    return True

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(splitArray(nums,m))
