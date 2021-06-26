# -*- coding: utf-8 -*-
# @File    : SelfDividingNumbers.py
# @Date    : 2021-06-26
# @Author  : tc
"""
题号 728. 自除数
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：

输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left,right + 1):
            copy = num
            while copy > 0:
                div, copy = copy % 10, copy // 10
                if div == 0 or num % div != 0: break
            else: ans.append(num) # while … else 在循环条件为 false 时执行 else 语句块
        return ans