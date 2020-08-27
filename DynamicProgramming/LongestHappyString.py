# -*- coding: utf-8 -*-
# @File    : LongestHappyString.py
# @Date    : 2020-08-28
# @Author  : tc
"""
题号 1405. 最长快乐字符串
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。



示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。


提示：

0 <= a, b, c <= 100
a + b + c > 0

参考：https://leetcode.com/problems/longest-happy-string/discuss/564248/Python-HEAP-solution-with-explanation

"""
from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))
        s = []
        while max_heap:
            first, char1 = heappop(max_heap)  # char with most rest numbers
            if len(s) >= 2 and s[-1] == s[-2] == char1:  # check whether this char is the same with previous two
                if not max_heap:  # if there is no other choice, just return
                    return ''.join(s)
                second, char2 = heappop(max_heap)  # char with second most rest numbers
                s.append(char2)
                second += 1  # count minus one, because the second here is negative, thus add 1
                if second != 0:  # only if there is rest number count, add it back to heap
                    heappush(max_heap, (second, char2))
                heappush(max_heap, (first, char1))  # also need to put this part back to heap
                continue

            #  situation that this char can be directly added to answer
            s.append(char1)
            first += 1
            if first != 0:
                heappush(max_heap, (first, char1))
        return ''.join(s)



if __name__ == '__main__':
    pass