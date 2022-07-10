# -*- coding: utf-8 -*-
# @File    : KThSmallestInLexicographicalOrder.py
# @Date    : 2022-07-11
# @Author  : tc
"""
440. 字典序的第K小数字
给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

示例 1:
输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

示例 2:
输入: n = 1, k = 1
输出: 1

字典树思想
https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/solution/zi-dian-xu-de-di-kxiao-shu-zi-by-leetcod-bfy0/
https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/solution/shi-cha-shu-by-powcai/
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def cal_steps(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return step

        cur = 1
        k -= 1

        while k > 0:
            steps = cal_steps(n, cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10

        return cur