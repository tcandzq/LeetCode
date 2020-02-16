# -*- coding: utf-8 -*-
# @File    : RandomPickIndex.py
# @Date    : 2020-02-16
# @Author  : tc
"""
题号 398 随机数索引
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

# 蓄水池抽样

"""
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        import random
        res = None
        count = 0
        for i,v in enumerate(self.nums):
            if v == target:
               if random.randint(0,count) == 0:
                    res = i
               count += 1
        return res

if __name__ == '__main__':
    solution = Solution([1,2,3,3,3])
    print(solution.pick(3))
