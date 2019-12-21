# -*- coding: utf-8 -*-
# @File    : LengthOfLastWord.py
# @Date    : 2019-12-21
# @Author  : tc
"""
题号 58 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

"""
class Solution:
    # 解法1
    def lengthOfLastWord(self, s: str) -> int:
        nums = s.split(' ')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]:
                return len(nums[i])
        return 0

    # 解法2
    def lengthOfLastWord2(self, s: str) -> int:
        s = s.strip(' ')  # strip只能删除字符串开头和结尾的空格
        print(s)
        L = s.split(' ')[-1]
        return len(L)
if __name__ == '__main__':
    s = "Hello World"
    solution = Solution()
    print(solution.lengthOfLastWord2(s))
