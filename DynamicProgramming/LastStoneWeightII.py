# -*- coding: utf-8 -*-
# @File    : LastStoneWeightII.py
# @Date    : 2020-07-08
# @Author  : tc
"""
题号 1049. 最后一块石头的重量II
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。



示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。


提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

思路：
经典的背包问题。等价于把所有的数装进两个袋子，然后分别计算两个袋子中所有数的和得到a和b，最后计算a和b差的最小值。

石头粉碎的所有情况都可以通过两个背包来表示。最后一个石头的重量等于这两个背包的差值。

用dp存储更小的那个背包的值

"""
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        sum_stones = sum(stones)
        for stone in stones:
            print(stone,dp)
            dp |= {stone + i for i in dp}
        return min(abs(sum_stones - i - i) for i in dp)


if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    solution = Solution()
    print(solution.lastStoneWeightII(stones))
