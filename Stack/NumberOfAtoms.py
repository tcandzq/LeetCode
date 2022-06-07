# -*- coding: utf-8 -*-
# @File    : NumberOfAtoms.py
# @Date    : 2022-06-08
# @Author  : tc
"""
726. 原子的数量
给你一个字符串化学式 formula ，返回 每种原子的数量 。

原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。

例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。
两个化学式连在一起可以构成新的化学式。

例如 "H2O2He3Mg4" 也是化学式。
由括号括起的化学式并佐以数字（可选择性添加）也是化学式。

例如 "(H2O2)" 和 "(H2O2)3" 是化学式。
返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1：
输入：formula = "H2O"
输出："H2O"
解释：原子的数量是 {'H': 2, 'O': 1}。

示例 2：
输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3：

输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

用栈求解,注意小写字母可连续，从后往前遍历会更加方便。
"""
import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                # 防止数字为2位数以上
                i += 1
            elif c == ")":
                stack.append(cnt or 1)  # 防止cnt 为0
                coeff *= cnt or 1  # 防止cnt 为0
                # stack.append(cnt)
                # coeff *= cnt
                i = cnt = 0
            elif c == "(":
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ""
                i = cnt = 0
            elif c.islower():
                elem += c
            print("dic is {}, coeff is {}, stack is {}, elem is {}, cnt is {}, i is {}, coeff is {}".format(dic, coeff, stack, elem, cnt, i, coeff))
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))