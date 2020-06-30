# -*- coding: utf-8 -*-
# @File    : CountDifferentPalindromicSubsequences.py
# @Date    : 2020-06-29
# @Author  : tc
"""
题号 730. 统计不同回文子序列
给定一个字符串 S，找出 S 中不同的非空回文子序列个数，并返回该数字与 10^9 + 7 的模。

通过从 S 中删除 0 个或多个字符来获得子序列。

如果一个字符序列与它反转后的字符序列一致，那么它是回文字符序列。

如果对于某个  i，A_i != B_i，那么 A_1, A_2, ... 和 B_1, B_2, ... 这两个字符序列是不同的。



示例 1：

输入：
S = 'bccb'
输出：6
解释：
6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
示例 2：

输入：
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：
共有 3104860382 个不同的非空回文子序列，对 10^9 + 7 取模为 104860361。


提示：

字符串 S 的长度将在[1, 1000]范围内。
每个字符 S[i] 将会是集合 {'a', 'b', 'c', 'd'} 中的某一个。

用DFS(start,end)表示字符串S[start,end]中的回文子序列的数量。

由于每个字符只能是集合 {'a', 'b', 'c', 'd'}中的某一个，不妨以字母"a"为例，计算以字母'a'为开头和结尾的字符串S[i,j]中回文子序列的数量
首先用i表示"a"首次出现的索引位置，用j表示"a"最后一次出现的索引位置，因此可以分为两种情况考虑：

1.如果i == j，意味着字符串S[i,j]只有一个字母"a"，所以回文子序列的数量就是1;
2.如果i != j，那么可能的回文子序列由'a','aa'和'a*a'组成，其中'*'表示S[i+1,j-1]中可能的回文子序列。此时回文子序列的数量就是DFS(i+1,j-1)+2,2表示'a'和'aa'

参考：https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109510/Python-DP%2BDFS-O(n2)-with-Explanations

"""

class Solution:

    def countPalindromicSubsequences(self, S: str) -> int:
        M = 1000000007

        def DFS(start, end, mem={}):
            if (start, end) in mem:
                return mem[(start, end)]

            count = 0
            s = S[start:end + 1]  # 注意这里end + 1
            for x in 'abcd':
                try:
                    i = s.index(x) + start
                    j = s.rindex(x) + start
                except:
                    continue

                count += DFS(i + 1, j - 1, mem) + 2 if i != j else 1
            mem[(start, end)] = count % M
            return mem[(start, end)]

        return DFS(0, len(S) - 1)


if __name__ == '__main__':
    S = 'bccb'
    solution = Solution()
    print(solution.countPalindromicSubsequences2(S))

