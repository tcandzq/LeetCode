# -*- coding: utf-8 -*-
# @File    : TotalHammingDistance.py
# @Date    : 2020-02-13
# @Author  : tc
"""
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

示例:

输入: 4, 14, 2

输出: 6

解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
注意:

数组中元素的范围为从 0到 10^9。
数组的长度不超过 10^4。

对每个数按对应的位统计，而不是按照数来统计
1.将每个数展开成32位，高位补0，比如4的二进制就是 '00000000000000000000000000000100'
2.按对每一位进行统计，考虑数组中每个数二进制的第 i 位，假设一共有 t 个 0 和 n - t 个 1，那么显然在第 i 位的汉明距离的总和为 t * (n - t)

参考：https://leetcode-cn.com/problems/total-hamming-distance/solution/yi-ming-ju-chi-zong-he-by-leetcode/

"""
from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))

if __name__ == '__main__':
    nums = [4, 14, 2]
    solution = Solution()
    print(solution.totalHammingDistance(nums))
    print(len(list(zip(map('{:032b}'.format, nums)))))
    print(list(zip(*map('{:032b}'.format, nums))))