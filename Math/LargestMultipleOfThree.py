# -*- coding: utf-8 -*-
# @File    : LargestMultipleOfThree.py
# @Date    : 2021-07-05
# @Author  : tc
"""
题号 1363. 形成三的最大倍数
给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。

由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。

如果无法得到答案，请返回一个空字符串。

示例 1：

输入：digits = [8,1,9]
输出："981"
示例 2：

输入：digits = [8,6,7,1,0]
输出："8760"
示例 3：

输入：digits = [1]
输出：""
示例 4：

输入：digits = [0,0,0,0,0,0]
输出："0"

1.首先如果每个数字和加起来是3，那么这些数字肯定能被3整除，从大到小排序所有数字组成字符串输出即可
2.如果数字和sum%3==2 那么去除掉最小的%3==2的数字，如果没有这类数字，则去除掉两个最小的%3==1的数字
3.sum%3==1 则类似于sum%3==2的思路即可

解法1:https://leetcode-cn.com/problems/largest-multiple-of-three/solution/xing-cheng-san-de-zui-da-bei-shu-by-leetcode-solut/

解法2:https://leetcode.com/problems/largest-multiple-of-three/discuss/517628/Python-Basic-Math

"""
from typing import List
import collections

class Solution:
    def largestMultipleOfThree1(self, digits: List[int]) -> str:
        cnt, modulo = [0] * 10, [0] * 3
        s = 0
        for digit in digits:
            cnt[digit] += 1
            modulo[digit % 3] += 1
            s += digit

        remove_mod, rest = 0, 0
        if s % 3 == 1:
            remove_mod, rest = (1, 1) if modulo[1] >= 1 else (2, 2)
        elif s % 3 == 2:
            remove_mod, rest = (2, 1) if modulo[2] >= 1 else (1, 2)

        ans = ""
        for i in range(0, 10):
            for j in range(cnt[i]):
                if rest > 0 and remove_mod == i % 3:
                    rest -= 1
                else:
                    ans += str(i)
        if len(ans) > 0 and ans[-1] == "0":
            ans = "0"
        return ans[::-1]

    def largestMultipleOfThree2(self, digits: List[int]) -> str:
        total = sum(digits)
        count = collections.Counter(digits)
        digits.sort(reverse=1)

        def fi(i):
            if count[i]:
                digits.remove(i)
                count[i] -= 1
            if not digits:
                return ''
            if not any(digits):
                return '0'
            if sum(digits) % 3 == 0:
                return ''.join(map(str, digits))

        if total % 3 == 0:
            return fi(-1)
        if total % 3 == 1 and count[1] + count[4] + count[7]:  # 如果1、4、7中任何一个元素在数组digits中,那就从小到大依次1、4、7
            return fi(1) or fi(4) or fi(7)
        if total % 3 == 2 and count[2] + count[5] + count[8]:  # 如果2、5、8中任何一个元素在数组digits中,那就从小到大依次2、5、8
            return fi(2) or fi(5) or fi(8)
        if total % 3 == 2:
            return fi(1) or fi(1) or fi(4) or fi(4) or fi(7) or fi(7)  # 如果1、4、7都不在数组digits中那就移除两个(1,4,7)中任一数值
        return fi(2) or fi(2) or fi(5) or fi(5) or fi(8) or fi(8)  # 如果2、5、8都不在数组digits中那就移除两个(2, 5, 8)中任一数值