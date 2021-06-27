# -*- coding: utf-8 -*-
# @File    : ReplaceElementsWithGreatestElementOnRightSide.py
# @Date    : 2021-06-28
# @Author  : tc
"""
题号 1299. 将每个元素替换为右侧最大元素
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

完成所有替换操作后，请你返回这个数组。

示例 1：

输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]
解释：
- 下标 0 的元素 --> 右侧最大元素是下标 1 的元素 (18)
- 下标 1 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 2 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 3 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 4 的元素 --> 右侧最大元素是下标 5 的元素 (1)
- 下标 5 的元素 --> 右侧没有其他元素，替换为 -1
示例 2：

输入：arr = [400]
输出：[-1]
解释：下标 0 的元素右侧没有其他元素。

从右往左遍历，先记录右边最大值 rightMax 为最后一个值，向左每次更新 rightMax，使用变量 t 先记住当前 arr[i] 就可以了。

参考：https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side/solution/jiang-mei-ge-yuan-su-ti-huan-wei-you-ce-zui-da-y-5/

"""
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans



