# -*- coding: utf-8 -*-
# @File    : 48_LongestSubstringWithoutDup.py
# @Date    : 2020-03-31
# @Author  : tc
"""
面试题48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

解法1 参考：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/pythonti-jie-shuang-100-dp-hua-dong-chuang-kou-shu/
解法2 参考：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        tail = 0
        result = 0
        for i in range(len(s)):
            if s[i] in dic:
                tail = max(dic[s[i]] + 1, tail)  # 优化步骤
            dic[s[i]] = i
            result = max(result, i - tail + 1)
        return result

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])
        return max_len




if __name__ == '__main__':
    s = 'abcabcbb'
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
