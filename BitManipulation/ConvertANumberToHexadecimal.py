# -*- coding: utf-8 -*-
# @File    : ConvertANumberToHexadecimal.py
# @Date    : 2022-08-21
# @Author  : tc
"""
405. 数字转换为十六进制数
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：
输入:
26
输出:
"1a"

示例 2：
输入:
-1
输出:
"ffffffff"


代码来自:https://leetcode.cn/problems/convert-a-number-to-hexadecimal/solution/pythonjava-2jin-zhi-zhuan-huan-wei-16jin-dwen/
"""
class Solution:
    def toHex(self, num: int) -> str:
        CONV = "0123456789abcdef"
        ans = []
        # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        for _ in range(8):
            # 当输入值num为-1 ，第一次进入循环
            ans.append(num % 16)  # num % 16 = 15
            num //= 16  # num // 16 = -1
            # Python中的//运算取整除：向下取接近商的整数
            # %取模运算返回整除的余数 （余数 = 被除数 - 除数 * 商）
            # 负整数 // 正整数 的最大值为-1
            #   -1 // 16 = -1
            #   -1 % 16 = 15
            #   即如num为负数，则一定会跑满for的8次循环
            # 正整数 // 正整数 的最小值为0
            #   1 // 16 = 0
            #   1 % 16 = 1
            #   即num为正数时，有可能触发下面的if语句，提前结束for循环
            if not num:  # 如果num不为0则继续下一次for循环
                break  # 如果num为0则终止for循环
            # 正整数 // 负整数 的最大值为-1，如1 // -16 = -1; 1 % -16 = -15
        return "".join(CONV[n] for n in ans[::-1])