#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 22:04
# @Author  : tc
# @File    : 3Sum.py
"""
题号 15 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

其实是三指针，但要固定一个指针，其他两个指针用双指针的方法，前提当然是数组已经排序了。

参考:https://leetcode-cn.com/problems/3sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/

本题的解法，可以作为两数之和、三数之和等系列问题甚至是双指针问题的模板写法

"""
from typing import List

class Solution:
    #  回溯超时
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        size = len(nums)
        res = []
        nums.sort()
        def dfs(i,tmp_sum,tmp_list):
            if tmp_sum == 0 and len(tmp_list) == 3:
                res.append(tmp_list)
                return
            for j in range(i,size):
                if tmp_sum + nums[j] > 0:
                    break
                if j > i and nums[j] == nums[j - 1]: continue
                dfs(j+1, tmp_sum+nums[j], tmp_list+[nums[j]])
        dfs(0,0,[])
        return res

    # 排序+双指针
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):  # 1.固定指针K，并不断遍历
            if nums[k] > 0:
                break  # 2. 已经排序了且 nums[i]>nums[j]>nums[k]
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 2. 相同的nums[k] 只会产生一个结果，且在nums[k-1]已经计算过了
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. 内核为双指针
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:  # 原因和2是一样的
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res




if __name__ == '__main__':
    nums = [-7,-5,5,-6,-2,1,7,3,-4,-2,-2,-4,-8,-1,8,8,-2, -7, 3,2,-7,8,-3,-10,5,2,8,7,7]
    solution = Solution()
    print(solution.threeSum2(nums))