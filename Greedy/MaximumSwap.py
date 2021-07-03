# -*- coding: utf-8 -*-
# @File    : MaximumSwap.py
# @Date    : 2021-07-03
# @Author  : tc
"""
题号 670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。

1.我们将计算 ast[d] = i，最后一次出现的数字d（如果存在）的索引i。
2.然后，从左到右扫描数字时，如果将来有较大的数字，我们将用最大的数字交换；如果有多个这样的数字，我们将用最开始遇到的数字交换。

参考：https://leetcode-cn.com/problems/maximum-swap/solution/zui-da-jiao-huan-by-leetcode/

代码参考：https://leetcode.com/problems/maximum-swap/discuss/107066/Python-Straightforward-with-Explanation

"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, 0) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num