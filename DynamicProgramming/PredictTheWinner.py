# -*- coding: utf-8 -*-
# @File    : PredictTheWinner.py
# @Date    : 2020-02-13
# @Author  : tc
"""
题号 486 预测赢家
给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1:

输入: [1, 5, 2]
输出: False
解释: 一开始，玩家1可以从1和2中进行选择。
如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
因此，玩家1永远不会成为赢家，返回 False。
示例 2:

输入: [1, 5, 233, 7]
输出: True
解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。
注意:

1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于10000000。
如果最终两个玩家的分数相等，那么玩家1仍为赢家。

用 dp(i, j) 表示当剩下的数为 nums[i .. j] 时，当前操作的选手（注意，不一定是先手）与另一位选手最多的分数差。当前操作的选手可以选择 nums[i] 并留下 nums[i+1 .. j]，或选择 nums[j] 并留下 nums[i .. j-1]，因此状态转移方程为：

dp(i, j) = max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))
dp(i, i) = nums[i]
如果 dp(0, n - 1) >= 0，那么先手必胜。

1.初始化时，dp[i][i] =nums[i]; 意味着如果只有一个nums[i]可以拿，先手玩家拿走了，nums[i] 也就是多出来的分数

2.dp[i][j]表示先手玩家从nums[i]拿到nums[j]时，比后手玩家多的最大分数

3.对于dp[i][j]来说，先手玩家有两种拿法，一种是拿开头的数，一种是拿结尾的数

4.如果先拿了nums[i]，也就是意味着先手玩家目前的分数是nums[i]+后手玩家获得的最大分数的相反值，也就是dp[i][j] = nums[i]+（-dp[i+1][j]）这里的dp[i+1][j]表示是后手玩家比先手玩家多的最大分数，

5.同理如果先拿了nums[j]，也就是意味着先手玩家目前的分数是nums[j]+后手玩家获得的最大分数的相反值，也就是dp[i][j] = nums[j]+（-dp[i][j-1]）这里的dp[i][j-1]表示是后手玩家比先手玩家多的最大分数
而每一步，先手玩家都想拿到最大的分数，最后才有机会赢，所以最终的转移方程是：dp[i][j] =max{nums[i]+（-dp[i+1][j]）, nums[j]+（-dp[i][j-1]）}

6.最后要求的值时dp[0][n-1]也就是dp的右上角的数，判断这个数是否大于0，大于0意味着先手玩家比后手玩家多，会赢
注意for loop的顺序，解释参加下图


参考:https://leetcode-cn.com/problems/predict-the-winner/solution/san-chong-dpsi-lu-jie-jue-duo-si-lu-by-a-fei-8/

"""
from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(nums[i] - dp[i+1][j],nums[j] - dp[i][j-1])
        return dp[0][n-1] > 0



if __name__ == '__main__':
    nums = [1, 5, 233, 7]
    solution = Solution()
    print(solution.PredictTheWinner(nums))