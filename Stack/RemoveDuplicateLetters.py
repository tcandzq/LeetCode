# -*- coding: utf-8 -*-
# @File    : RemoveDuplicateLetters.py
# @Date    : 2020-02-22
# @Author  : tc
"""
题号 316. 去除重复字母
给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"

贪心+单调递增栈

参考：https://leetcode-cn.com/problems/remove-duplicate-letters/solution/zhan-by-liweiwei1419/

"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        last_appear_index = [0 for _ in range(26)]
        for i in range(n):
            last_appear_index[ord(s[i]) - 97] = i

        stack = []
        for i in range(n):
            if s[i] in stack:
                continue
            while stack and ord(stack[-1]) > ord(s[i]) and last_appear_index[ord(stack[-1]) - 97] >= i :
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)




if __name__ == '__main__':
    s = "cbacdcbc"
    solution = Solution()
    print(solution.removeDuplicateLetters(s))