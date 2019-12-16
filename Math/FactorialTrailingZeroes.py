# -*- coding: utf-8 -*-
# @File    : FactorialTrailingZeroes.py
# @Date    : 2019-12-16
# @Author  : tc
"""
题号 172 阶乘后的零
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

参考：https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/

"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += int(n / 5)
            n /= 5
        return count

    # 耗时优化
    def trailingZeroes2(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n // 5
            n //= 5
        return count


if __name__ == '__main__':
    n = 9
    solution = Solution()
    print(solution.trailingZeroes(n))