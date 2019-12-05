#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 15:02
# @Author  : tc
# @File    : CountPrimes.py
"""
题号 204 计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

思路参考:https://leetcode-cn.com/problems/count-primes/solution/ru-he-gao-xiao-pan-ding-shai-xuan-su-shu-by-labula/

代码参考:https://leetcode-cn.com/problems/count-primes/solution/qiu-zhi-shu-chao-guo-90-by-powcai/
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        is_prim = [1] * n
        is_prim[0] = is_prim[1] = 0
        for i in range(2, int(n ** 0.5)+1):
            if is_prim[i]:
                is_prim[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(is_prim)



if __name__ == '__main__':
    n = 100
    solution = Solution()
    print(solution.countPrimes(n))
