# -*- coding: utf-8 -*-
# @File    : NonNegativeIntegersWithoutConsecutiveOnes.py
# @Date    : 2022-06-19
# @Author  : tc
"""
600. 不含连续1的非负整数
给定一个正整数 n ，返回范围在 [0, n] 都非负整数中，其二进制表示不包含 连续的 1 的个数。
示例 1:

输入: n = 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
示例 2:

输入: n = 1
输出: 2
示例 3:

输入: n = 2
输出: 3

数位DP解法,长度为n的二进制数字中不含连续1的非负整数个数满足斐波那契数列。
"""

class Solution:
    def findIntegers(self, n: int) -> int:
        # f stores the fibonacci numbers
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1] + f[-2])

        # last_seen tells us if there was a one right before.
        # If that is the case, we are done then and there!
        # ans is the answer
        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1 << i) & n:  # is the ith bit set?
                ans += f[i]
                if last_seen:
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans + 1