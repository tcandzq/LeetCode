# -*- coding: utf-8 -*-
# @File    : ContinuousSubarraySum.py
# @Date    : 2020-02-12
# @Author  : tc
"""
题号 523 连续的子数组和
给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例 1:

输入: [23,2,4,6,7], k = 6
输出: True
解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2:

输入: [23,2,6,4,7], k = 6
输出: True
解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
说明:

数组的长度不会超过10,000。
你可以认为所有数字总和在 32 位有符号整数范围内。

"""
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        temp = [0]  # 前置一个0防止得不到前两个数的和
        _temp = 0
        for num in nums:
            _temp += num
            temp.append(_temp)
        for i in range(n+1):
            for j in range(i+2,n+1):
                _sum = temp[j] - temp[i]
                if k == 0:
                    if _sum == 0: return True
                else:
                    if _sum % k == 0: return True
        return False


if __name__ == '__main__':
    nums = [0,0]
    k = 0
    solution = Solution()
    print(solution.checkSubarraySum(nums,k))