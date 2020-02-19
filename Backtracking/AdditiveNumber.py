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

"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n//2 + 1):
            if num[0] == '0' and i > 1:
                return False
            x1 = int(num[:i])
            for j in range(1,n):
                if max(j,i) > n - i - j:
                    break
                if num[i] == '0' and j > 1:
                    break
                x2 = int(num[i:i+j])
                if self.is_valid(x1,x2,j+i,num):
                    return True
        return False

    def is_valid(self, x1: int, x2: int, start: int, num: str):
        if start == len(num):
            return True
        x2 = x2 + x1
        x1 = x2 - x1
        _sum = str(x2)
        return num.startswith(_sum,start) and self.is_valid(x1,x2,start+len(_sum), num)

if __name__ == '__main__':
    num = "199100199"
    solution = Solution()
    print(solution.isAdditiveNumber(num))