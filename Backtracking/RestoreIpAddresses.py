# -*- coding: utf-8 -*-
# @File    : RestoreIpAddresses.py
# @Date    : 2021-06-28
# @Author  : tc
"""
93. 复原IP地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。



示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

经典的回溯算法

思路参考：https://leetcode-cn.com/problems/restore-ip-addresses/solution/hui-su-suan-fa-hua-tu-fen-xi-jian-zhi-tiao-jian-by/

"""
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, ct, path, rst):
            if ct == 4:
                # have 4 chunk and use up all digits
                if not s: rst.append(path[:-1])
                return
            for i in range(1, 4):
                # prevent index overflow
                if i > len(s): continue
                # take 1 digit is always good
                # take 2 or 3 digits, first digit cannot be '0'
                if i > 1 and s[0] == '0': continue
                # take 3 digits, cannot greater than 255
                if i > 2 and int(s[:3]) > 255: continue
                backtrack(s[i:], ct + 1, path + s[:i] + '.', rst)

        rst = []
        backtrack(s, 0, '', rst)
        return rst