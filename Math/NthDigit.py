# -*- coding: utf-8 -*-
# @File    : NthDigit.py
# @Date    : 2020-02-21
# @Author  : tc
"""
题号 400 第N个数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。

代码1参考：https://leetcode-cn.com/problems/nth-digit/solution/xiang-jie-zhao-gui-lu-by-z1m/

代码2参考：https://leetcode.com/problems/nth-digit/discuss/88375/Short-Python%2BJava

"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 9
        digits = 1
        while n - base*digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        idx = n % digits
        if idx == 0:
            idx = digits
        number = 1
        for i in range(1,digits):
            number *= 10
        if idx == digits:
            number += n // digits - 1
        else:
            number += n // digits
        for i in range(idx,digits):
            number //= 10
        return number % 10

    def findNthDigit2(self, n: int) -> int:
        n -= 1
        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n / digits)[n % digits])
            n -= 9 * first * digits





if __name__ == '__main__':
    n = 19
    solution = Solution()
    print(solution.findNthDigit(n))