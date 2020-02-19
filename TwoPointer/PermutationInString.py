# -*- coding: utf-8 -*-
# @File    : PermutationInString.py
# @Date    : 2020-02-19
# @Author  : tc

"""
题号 567 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

优化的滑动窗口参考：https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation

"""
class Solution:
    # 滑动窗口
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        count_dict = collections.Counter(s1)
        m = len(s1)
        i = 0
        j = m - 1
        while j < len(s2):
            if collections.Counter(s2[i:j+1]) == count_dict:
                return True
            i += 1
            j += 1
        return False

    # 优化的滑动窗口
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        print(A,B)
        target = [0] * 26
        for x in A:
            target[x] += 1
        print(target)
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidboaoo"
    solution = Solution()
    print(solution.checkInclusion2(s1,s2))