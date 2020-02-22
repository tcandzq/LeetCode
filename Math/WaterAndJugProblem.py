# -*- coding: utf-8 -*-
# @File    : WaterAndJugProblem.py
# @Date    : 2020-02-22
# @Author  : tc
"""
365 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False

设z = a * x + b * y;（a和b是整数有且可能是负数）假设x和y的最大公约数为g.

且 x = m * g, y = n * g; 则等式变为 z = (a * m + b * n) * g;

要想等式成立则z必需能被x和y的最大公约数整除。z % g = 0;

参考链接 https://blog.csdn.net/qq_40636117/article/details/80340421


"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or x + y == z:
            return True

        if not x or not y or x + y < z:
            return False
        return z % self.find_divisor(x,y) == 0

    def find_divisor(self,a,b):
        if a < b:
            a,b = b,a
        if a % b == 0:
            return b
        else:
            return self.find_divisor(a,a%b)

    def find_divisor2(self, a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return b


if __name__ == '__main__':
    x = 3
    y = 5
    z = 4
    solution = Solution()
    print(solution.canMeasureWater(x,y,z))
    print(solution.find_divisor2(88,24))