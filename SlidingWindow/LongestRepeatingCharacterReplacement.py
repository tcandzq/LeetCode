# -*- coding: utf-8 -*-
# @File    : LongestRepeatingCharacterReplacement.py
# @Date    : 2020-02-24
# @Author  : tc
"""
题号 424. 替换后的最长重复字符
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:

输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
示例 2:

输入:
s = "AABABBA", k = 1

输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

思路参考：https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/

代码参考：https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation

"""
import collections
class Solution:

    def characterReplacement(self, s, k):
        count = [0] * 26
        max_count = start = result = 0
        for end in range(len(s)):
            index = ord(s[end]) - ord('A')
            count[index] += 1
            max_count = max(max_count, count[ord(s[end]) - ord('A')])
            if end - start + 1 > max_count + k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result



if __name__ == '__main__':
    s = "AABABBA"
    solution = Solution()
    print(solution.characterReplacement(s,2))



