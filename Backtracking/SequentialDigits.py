# -*- coding: utf-8 -*-
# @File    : SequentialDigits.py
# @Date    : 2020-02-29
# @Author  : tc
"""
题号 1291. 顺次数
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。

请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。



示例 1：

输出：low = 100, high = 300
输出：[123,234]
示例 2：

输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]


提示：

10 <= low <= high <= 10^9

参考：https://leetcode.com/problems/sequential-digits/discuss/451849/JavaPython-3-Simple-codes.

"""
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for digit in range(1,9):
            num = next = digit
            while num <= high and next < 10:
                if num >= low:
                    ans.append(num)
                next += 1
                num = num * 10 + next
        return sorted(ans)


    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        res = []
        def dfs(cur,low,high):
            if cur*10 + (cur % 10 + 1) > high or cur % 10 in [0,9]:
                return
            res.append(cur*10 + (cur % 10 + 1))
            dfs(cur*10 + (cur % 10 + 1),low,high)
        for i in range(1,10):
            dfs(i,low,high)
        return list(sorted([num for num in res if low < num]))


if __name__ == '__main__':
    low = 1000
    high = 13000
    solution = Solution()
    print(solution.sequentialDigits(low,high))





