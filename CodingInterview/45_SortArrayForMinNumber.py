# -*- coding: utf-8 -*-
# @File    : 45_SortArrayForMinNumber.py
# @Date    : 2020-05-11
# @Author  : tc
"""
面试题45. 把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

参考：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/

"""
from typing import List
import functools

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x,y):
            a,b = x+y,y+x
            if a > b:return 1
            elif a <b : return -1
            else:return 0
        s = [str(num) for num in nums]
        s.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(s)


