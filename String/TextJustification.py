# -*- coding: utf-8 -*-
# @File    : TextJustification.py
# @Date    : 2019-12-22
# @Author  : tc
"""
题号 68 文本左右对齐

给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

参考：https://leetcode-cn.com/problems/text-justification/solution/shun-zhao-si-lu-xiang-by-powcai/

"""
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0

        def one_row_words(i):
            # 至少 一行能放下一个单词, cur_row_len
            left = i
            cur_row_len = len(words[i])
            i += 1
            while i < n:
                # 当目前行 加上一个单词长度 再加一个空格
                if cur_row_len + len(words[i]) + 1 > maxWidth:
                    break
                cur_row_len += len(words[i]) + 1
                i += 1
            return left, i

        while i < n:
            left, i = one_row_words(i)
            # 该行几个单词获取
            one_row = words[left:i]
            # 如果是最后一行了
            if i == n:
                res.append(" ".join(one_row).ljust(maxWidth, " "))
                break
            # 所有单词的长度
            all_word_len = sum(len(i) for i in one_row)
            # 至少空格个数
            space_num = i - left - 1
            # 可以为空格的位置
            remain_space = maxWidth - all_word_len
            # 单词之间至少几个空格,还剩几个空格没用
            if space_num:
                a, b = divmod(remain_space, space_num)
            # print(a,b)
            # 该行字符串拼接
            tmp = ""
            for word in one_row:
                if tmp:
                    tmp += " " * a
                    if b:
                        tmp += " "
                        b -= 1
                tmp += word
            # print(tmp, len(tmp))
            res.append(tmp.ljust(maxWidth, " "))
        return res



if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    solution = Solution()
    print(solution.fullJustify(words,16))