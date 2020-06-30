# -*- coding: utf-8 -*-
# @File    : ReducingDishes.py
# @Date    : 2020-06-30
# @Author  : tc
"""
题号 1402. 做菜顺序
一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1单位时间。

一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。

请你返回做完所有菜 「喜爱时间」总和的最大值为多少。

你可以按任意顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

示例 1：

输入：satisfaction = [-1,-8,0,5,-9]
输出：14
解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。
示例 2：

输入：satisfaction = [4,3,2]
输出：20
解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)
示例 3：

输入：satisfaction = [-1,-4,-5]
输出：0
解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。
示例 4：

输入：satisfaction = [-2,5,-1,0,3,-3]
输出：35

提示：

n == satisfaction.length
1 <= n <= 500
-10^3 <= satisfaction[i] <= 10^3

贪心：**满意程度越高的菜越往后做，喜爱时间总和就越大！**

每次我们在菜单上增加一道新菜，菜单上的所有菜都将在一个单位后完成，所以有`res += total`，`total`表示当前已经做的菜的喜爱值的和。

先对`satisfaction`进行排序，因此只要`satisfaction[-1] + total > 0` 那么喜爱时间总和就一直变大。。

"""
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res

if __name__ == '__main__':
    satisfaction = [-2, 5, -1, 0, 3, -3]
    solution = Solution()
    print(solution.maxSatisfaction(satisfaction))