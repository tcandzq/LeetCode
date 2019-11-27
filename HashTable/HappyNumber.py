#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 19:10
# @Author  : tc
# @File    : HappyNumber.py
"""
题号202 快乐数
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

注意理解题意,里面说了不管是不是快乐数,一定会循环下去

思路参考1:https://leetcode-cn.com/problems/happy-number/solution/shi-yong-kuai-man-zhi-zhen-si-xiang-zhao-chu-xun-h/
代码参考2:https://leetcode-cn.com/problems/happy-number/solution/ha-xi-huo-zhe-kuai-man-pao-by-powcai/

"""
class Solution:
    # hash解法
    def isHappy(self, n: int) -> bool:
        n = str(n)
        visited = set()
        while True:
            n = str(sum(int(i)**2 for i in n))
            if n == "1":
                return True
            if n in visited:
                return False
            visited.add(n)

    # 快慢指针解法
    def isHappy2(self, n: int) -> bool:
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
        return slow == "1"  # 因为当进入无限循环时,有两种情况,一种是slow = fast = 1,1^2 = 1;另外一种是slow = fast !=1


if __name__ == '__main__':
    n = 19
    solution = Solution()
    print(solution.isHappy(n))
