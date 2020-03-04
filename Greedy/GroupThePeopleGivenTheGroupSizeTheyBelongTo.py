# -*- coding: utf-8 -*-
# @File    : GroupThePeopleGivenTheGroupSizeTheyBelongTo.py
# @Date    : 2020-03-03
# @Author  : tc
"""
题号 1282. 用户分组
有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都恰好属于某一用户组。给你一个长度为 n 的数组 groupSizes，其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。

你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。

示例 1：

输入：groupSizes = [3,3,3,3,3,1,3]
输出：[[5],[0,1,2],[3,4,6]]
解释：
其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。
示例 2：

输入：groupSizes = [2,1,3,3,3,2]
输出：[[1],[0,5],[2,3,4]]


提示：

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""
from typing import List
import collections

class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)

        for i,_id in enumerate(groupSizes):
            groups[_id].append(i)

        ans = list()
        for gsize, users in groups.items():
            for it in range(0,len(users),gsize):
                ans.append(users[it:it+gsize])

        return ans

    def groupThePeople2(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i,groupSize in enumerate(groupSizes):
            if groupSize in d:
                d[groupSize].append(i)
            else:
                d[groupSize] = [i]
        print(d)
        res = []
        for key,val in d.items():
            if not len(val) % key:
                for i in range(1,len(val) // key+1):
                    res.append(val[key*(i-1):key*i])
        return res

if __name__ == '__main__':
    groupSizes = [2, 1, 3, 3, 3, 2]
    solution = Solution()
    print(solution.groupThePeople(groupSizes))
