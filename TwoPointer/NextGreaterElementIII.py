# -*- coding: utf-8 -*-
# @File    : NextGreaterElementIII.py
# @Date    : 2021-07-03
# @Author  : tc
"""
题号 556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：

输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1

1.从右往左遍历 找到第一个不是顺序排列的数字,而不是第一个比最右的数小的数

2.找到了这个数i之后再最后的数开始往右遍历,找到第一个比i大的数j与i交换,然后再对i后面的所有数重新排序


代码参考：https://leetcode.com/problems/next-greater-element-iii/discuss/983076/Python-O(m)-solution-explained

"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 1
        while i - 1 >= 0 and digits[i] <= digits[i - 1]:
            i -= 1

        if i == 0: return -1
        print(i, digits[i])
        j = i  # i 是后一个数
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1
        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))

        return ret if ret < 1 << 31 else -1