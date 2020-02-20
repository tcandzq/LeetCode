# -*- coding: utf-8 -*-
# @File    : AdditiveNumber.py
# @Date    : 2020-02-19
# @Author  : tc
"""
题号 306 累加数
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199

第一个数定义为num[:i]，包括num[0],但不包括num[i]。
当第一个数和任意长度的第二个数相加，一定会得到一个和，这个和的长度至少和第一个数一样长。
因此，第一个数的长度不可能超过给定字符串num长度的一半
因此，当i达到(n/2)+1时，我们可以停止迭代
注意到，当len(num) < 2时，循环退出

代码参考：https://leetcode.com/problems/additive-number/discuss/75567/Java-Recursive-and-Iterative-Solutions

"""
class Solution:
    # 带注释详细版
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        # 迭代所有可能的第一个数
        # 第一个数定义为num[:i]
        for i in range(1,  n//2 + 1):
            # 迭代所有可能的第二个数
            # 第二个数定义为num[i:i+j]
            # 当第二个数加到任意长度的第一个数，肯定会得到一个长度至少为max(i,j)的和sum
            # n是num的长度，i是第一个数，j是第二个数，那么(n - i - j)就是sum对应的数字
            # 由于sum的长度至少为max(i,j)，因此当max(i,j)大于n - i - j时，我们可以停止迭代
            for j in range(1, n):
                if max(i, j) > n - i - j:
                    break
                if self.is_valid(i, j, num):
                    return True
        return False

    def is_valid(self, i: int, j: int,  num: str): # 第一个数的长度是i，第二个数的长度是j,从num[i]开始
        # 检查第一个数中的leading zero
        # 第一个数允许为0，但此时它的长度不能超过1
        if num[0] == '0' and i > 1: return False
        # 第二个数允许为0，但此时它的长度不能超过1
        if num[i] == '0' and j > 1 : return False
        # 第一个数
        b1 = int(num[:i])
        # 第二个数
        b2 = int(num[i:i+j])
        # (1)计算第一个数和第二个数的和sum
        # (2)将第二个数更新为sum
        # (3)将第一个数更新为未更新前的第二个数
        # (4)检查num里的下一个数是不是sum
        # (5) 重复循环，直到下一个sum的起始下标超过了num的最后一个索引
        offset = i + j
        while offset < len(num):
            # 第二个数变成了第一个数和第二个数的和
            b2 = b2 + b1
            # 第一个数变成了第二个数
            b1 = b2 - b1
            _sum = str(b2)
            # 检查num的下一个数字
            if not num.startswith(_sum, offset): return False
            # offset的增加量是上一次的和_sum的长度
            offset += len(_sum)
        return True

    # 不带注释+尾递归版
    def isAdditiveNumber2(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i > 1:
                return False
            x1 = int(num[:i])
            for j in range(1, n):
                if max(j, i) > n - i - j:
                    break
                if num[i] == '0' and j > 1:
                    break
                x2 = int(num[i:i + j])
                if self.is_valid2(x1, x2, j + i, num):
                    return True
        return False

    def is_valid2(self, x1: int, x2: int, start: int, num: str):
        if start == len(num):
            return True
        x2 = x2 + x1
        x1 = x2 - x1
        _sum = str(x2)
        return num.startswith(_sum, start) and self.is_valid2(x1, x2, start + len(_sum), num)


if __name__ == '__main__':
    num = "199100199"
    solution = Solution()
    print(solution.isAdditiveNumber(num))