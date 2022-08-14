# -*- coding: utf-8 -*-
# @File    : PowerOfFour.py
# @Date    : 2022-08-14
# @Author  : tc
"""
342. 4的幂
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
示例 1：

输入：n = 16
输出：true
示例 2：

输入：n = 5
输出：false
示例 3：

输入：n = 1
输出：true

取模性质
如果n是4的幂，那么它可以表示成 4^x 的形式，我们可以发现它除以3的余数一定为1，即：

如果n是2的幂却不是4的幂，那么它可以表示成4^x x 2 的形式，此时它除以3的余数一定为 2。
因此我们可以通过 n除以3的余数是否为 1来判断n是否是4的幂。

参考：https://leetcode.cn/problems/power-of-four/solution/4de-mi-by-leetcode-solution-b3ya/
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1