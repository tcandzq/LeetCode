# -*- coding: utf-8 -*-
# @File    : 1BitAnd2BitCharacters.py
# @Date    : 2022-08-14
# @Author  : tc
"""
717. 1 比特与 2 比特字符
有两种特殊字符：

第一种字符可以用一比特 0 表示
第二种字符可以用两比特（10 或 11）表示
给你一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。

示例 1:
输入: bits = [1, 0, 0]
输出: true
解释: 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。

示例 2:
输入：bits = [1,1,1,0]
输出：false
解释：唯一的解码方式是将其解析为两比特字符和两比特字符。
所以最后一个字符不是一比特字符。


提示:
1 <= bits.length <= 1000
bits[i] 为 0 或 1

有两种字符串，一种是 0，一种是 10 或 11。即一种长度是1，一种长度是2.
所以找个指针然后遍历一遍：
遇到 0 走一步；
遇到 1走两步。
​
参考：https://leetcode.cn/problems/1-bit-and-2-bit-characters/solution/fu-xue-ming-zhu-tu-jie-suan-fa-zou-yi-bu-shvh/
"""
from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pos = 0
        while pos < len(bits) - 1:
            if bits[pos] == 1:
                pos += 2
            else:
                pos += 1
        return pos == len(bits) - 1