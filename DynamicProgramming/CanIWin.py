# -*- coding: utf-8 -*-
# @File    : CanIWin.py
# @Date    : 2020-02-14
# @Author  : tc
"""
题号 464 我能赢吗
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

参考：https://leetcode.com/problems/can-i-win/discuss/95292/Python-solution-easy-to-understand

"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1+maxChoosableInteger) * (maxChoosableInteger) // 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(list(range(1,maxChoosableInteger+1)),desiredTotal)

    def helper(self,nums,desiredTotal):
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]
        # 边界情况
        if nums[-1] >= desiredTotal:
            return True
        # 我选一个数，
        for i in range(len(nums)):
            # 轮到对手在剩下的数中选择一个数，如果对手没有赢，意味着我赢了
            if not self.helper(nums[:i]+nums[i+1:],desiredTotal-nums[i]):
                self.memo[hash] = True
                return True
        # 选不了任何数使得我赢
        self.memo[hash] = False
        return False

if __name__ == '__main__':
    maxChoosableInteger = 10
    desiredTotal = 11
    solution = Solution()
    print(solution.canIWin(maxChoosableInteger,desiredTotal))