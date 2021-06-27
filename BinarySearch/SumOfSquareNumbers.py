# -*- coding: utf-8 -*-
# @File    : SumOfSquareNumbers.py
# @Date    : 2021-06-27
# @Author  : tc
"""
题号 633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：

输入：c = 3
输出：false
示例 3：

输入：c = 4
输出：true
示例 4：

输入：c = 2
输出：true
示例 5：

输入：c = 1
输出：true

双指针，关键是确定a和b的取值范围为[0,sqrt(c)]

参考:https://leetcode-cn.com/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/

https://leetcode-cn.com/problems/sum-of-square-numbers/solution/gong-shui-san-xie-yi-ti-san-jie-mei-ju-s-7qi5/

"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(c**0.5)
        while low<=high:
            sumOf = low*low+high*high
            if sumOf==c: return True
            elif sumOf<c: low += 1
            else: high -= 1
        return False