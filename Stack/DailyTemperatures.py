#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 12:14
# @Author  : tc
# @File    : DailyTemperatures.py
"""
题号:739 每日温度
根据每日气温列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

本题和84题、85题一样都是利用单调栈的方法

关键是如何拿出当前元素的左边第一个大于该元素的索引,这时需要为一个从栈底到栈顶的一个单调递减的单调栈

单调栈详解+动态规划解法参考:https://leetcode-cn.com/problems/daily-temperatures/solution/dan-diao-zhan-dong-tai-gui-hua-gua-he-xin-shou-de-/

"""
from typing import List

class Solution:
    # 暴力法(超时)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T or len(T) == 1:
            return [0]
        res = [0] * len(T)
        print(res)
        for i in range(len(T)):
            for j in range(i+1,len(T)):
                if T[j] > T[i]:
                    res[i] = j-i
                    break
        return res

    # 单调栈解法
    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*len(T)
        p = 0
        while p < len(T):
            if not stack:
                stack.append(p)
                p += 1
            else:
                if T[p] > T[stack[-1]]:
                    res[stack[-1]] = p - stack[-1]
                    stack.pop()  # 因为维护的是一个单调递减栈,当前元素大于栈顶元素时,下一轮需要比较当前元素与弹栈之后的栈顶元素,而不是做p += 1的操作
                else:
                    stack.append(p)
                    p += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures2(T))