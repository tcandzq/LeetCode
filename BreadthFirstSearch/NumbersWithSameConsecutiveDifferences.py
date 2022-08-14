# -*- coding: utf-8 -*-
# @File    : NumbersWithSameConsecutiveDifferences.py
# @Date    : 2022-08-14
# @Author  : tc
"""
967. 连续差相同的数字
返回所有长度为 n 且满足其每两个连续位上的数字之间的差的绝对值为k的非负整数 。
请注意，除了 数字 0 本身之外，答案中的每个数字都 不能 有前导零。例如，01 有一个前导零，所以是无效的；但 0 是有效的。
你可以按 任何顺序 返回答案。

示例 1：

输入：n = 3, k = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。
示例 2：

输入：n = 2, k = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
示例 3：

输入：n = 2, k = 0
输出：[11,22,33,44,55,66,77,88,99]
示例 4：

输入：n = 2, k = 2
输出：[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]

提示：

2 <= n <= 9
0 <= k <= 9

We initial the current result with all 1-digit numbers,
like cur = [1, 2, 3, 4, 5, 6, 7, 8, 9].

Each turn, for each x in cur,
we get its last digit y = x % 10.
If y + K < 10, we add x * 10 + y + K to the new list.
If y - K >= 0, we add x * 10 + y - K to the new list.
We repeat this step N - 1 times and return the final result.

代码参考：
https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/211183/JavaC%2B%2BPython-Iterative-BFS-Solution
"""
from typing import List
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = range(1, 10)
        for i in range(1, n):
            cur2 = []
            for x in cur:
                y = x % 10
                if y + k <10:
                    cur2.append(x * 10 + y + k)
                if k > 0 and y - k >= 0:
                    cur2.append(x * 10 +y - k)
            cur = cur2
        return cur