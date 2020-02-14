# -*- coding: utf-8 -*-
# @File    : MatchsticksToSquare.py
# @Date    : 2020-02-14
# @Author  : tc
"""
题号 473 火柴拼正方形
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。
注意:

给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。

思路：
这个问题等价于将数组nums，划分成和相等的四个子集
因此可以把每个火柴放入可能的子集中进行尝试

参考:https://leetcode.com/problems/matchsticks-to-square/solution/

trick:
将数组逆序，可以加速，例如[8,4,4,4]，理论上可以得到边长为5的正方形，但由于8太长了，不符合要求，后面也就不需要判断了。

"""
from typing import List

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        perimeter = sum(nums)
        possible_side = perimeter // 4
        if possible_side * 4 != perimeter:
            return False
        sums = [0] * 4
        nums.sort(reverse=True)

        def dfs(index):
            if index == len(nums):
                return sums[0] == sums[1] == sums[2] == possible_side
            for i in range(4):
                if sums[i] + nums[index] <= possible_side:  # 起到了剪枝的作用，提前跳出
                    sums[i] += nums[index]
                    if dfs(index+1):  # 起到了剪枝的作用，提前跳出
                        return True
                    sums[i] -= nums[index]
            return False
        return dfs(0)

if __name__ == '__main__':
    nums = [1,1,2,2,2]
    solution = Solution()
    print(solution.makesquare(nums))