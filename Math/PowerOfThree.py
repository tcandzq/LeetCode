# -*- coding: utf-8 -*-
# @File    : PowerOfThree.py
# @Date    : 2019-12-16
# @Author  : tc

"""
题号 326 3的幂
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？

参考：https://leetcode-cn.com/problems/power-of-three/solution/di-gui-he-xun-huan-by-powcai/

"""
class Solution:
    # 解法一：丑陋版
    def isPowerOfThree(self, n: int) -> bool:
        if not n: return False
        while n != 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

    # 解法一：优雅版
    def isPowerOfThree2(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

    # 解法二：递归
    def isPowerOfThree3(self, n: int) -> bool:
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n // 3)))

    # 解法三
    def isPowerOfThree4(self, n: int) -> bool:
        return n > 0 and (1162261467 % n == 0)

if __name__ == '__main__':
    n = 9
    solution = Solution()
    print(solution.isPowerOfThree(n))
