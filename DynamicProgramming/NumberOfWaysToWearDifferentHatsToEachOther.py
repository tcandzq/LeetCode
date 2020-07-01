# -*- coding: utf-8 -*-
# @File    : NumberOfWaysToWearDifferentHatsToEachOther.py
# @Date    : 2020-06-30
# @Author  : tc
"""
题号 1434. 每个人戴不同帽子的方案数
总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。

给你一个整数列表的列表 hats，其中hats[i] 是第i个人所有喜欢帽子的列表。

请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。

由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。



示例 1：

输入：hats = [[3,4],[4,5],[5]]
输出：1
解释：给定条件下只有一种方法选择帽子。
第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。
示例 2：

输入：hats = [[3,5,1],[3,5]]
输出：4
解释：总共有 4 种安排帽子的方法：
(3,5)，(5,3)，(1,3) 和 (1,5)
示例 3：

输入：hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
输出：24
解释：每个人都可以从编号为 1 到 4 的帽子中选。
(1,2,3,4) 4 个帽子的排列方案数为 24 。
示例 4：

输入：hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
输出：111


提示：

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] 包含一个数字互不相同的整数列表。
"""
from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        num_of_people = len(hats)
        hat_to_people = [[] for i in range(41)]
        dp = [[-1 for i in range(2 ** num_of_people)] for j in range(41)]

        for i in range(num_of_people):
            for hat in hats[i]:
                hat_to_people[hat].append(i)
        return self.dfs(hat_to_people, dp, (1 << num_of_people) - 1, 1, 0)

    def dfs(self,hat_to_people:List[List[int]],dp:List[List[int]],all_assigned:int,hat:int,cur_assignment:int)->int:
        if cur_assignment == all_assigned:
            return 1
        if hat > 40:
            return 0
        if dp[hat][cur_assignment] != -1:
            return dp[hat][cur_assignment]
        res = self.dfs(hat_to_people,dp,all_assigned,hat+1,cur_assignment)
        for people in hat_to_people[hat]:
            if ((cur_assignment >> people) & 1) == 1:
                continue
            res += self.dfs(hat_to_people, dp, all_assigned, hat + 1, cur_assignment | (1 << people))
            res %= 10 ** 9 + 7

        dp[hat][cur_assignment] = res
        return res


if __name__ == '__main__':
    hats = [[3,5,1],[3,5]]
    solution = Solution()
    print(solution.numberWays(hats))


