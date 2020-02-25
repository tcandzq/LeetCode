# -*- coding: utf-8 -*-
# @File    : PartitionLabels.py
# @Date    : 2020-02-25
# @Author  : tc
"""
题号 763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

示例 1:

输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
注意:

S的长度在[1, 500]之间。
S只包含小写字母'a'到'z'。

参考：https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation

"""
from typing import List

class Solution:
    # 参考代码
    def partition_labels(self,S:str)-> List[int]:
        rightmost = {c:i for i,c in enumerate(S)}
        left,right = 0,0

        result = []
        for i,letter in enumerate(S):
            right = max(right,rightmost[letter])

            if i == right:
                result += [right - left + 1]
                left = right + 1
        return result


    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        last_appear_index = [0] * 26
        for i in range(n):
            last_appear_index[ord(S[i]) - ord('a')] = i
        j = 0
        res = []
        while j < n:
            start = j
            last_index = last_appear_index[ord(S[j]) - ord('a')]
            while j <= last_index:
                last_index = max(last_appear_index[ord(S[j]) - ord('a')],last_index)
                j += 1
            res.append(last_index - start + 1)
        return res


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    solution = Solution()
    print(solution.partitionLabels(S))