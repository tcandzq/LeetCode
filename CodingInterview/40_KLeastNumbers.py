# -*- coding: utf-8 -*-
# @File    : 40_KLeastNumbers.py
# @Date    : 2020-05-13
# @Author  : tc
"""
面试题40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

参考：BFPRT算法原理 https://zhuanlan.zhihu.com/p/31498036

"""
from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]


    # BFPRT算法
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]
