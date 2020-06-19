# -*- coding: utf-8 -*-
# @File    : SuperEggDrop.py
# @Date    : 2020-06-07
# @Author  : tc
"""
题号 887. 鸡蛋掉落
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？


示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1。
如果它没碎，那么我们肯定知道 F = 2。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
示例 3：

输入：K = 3, N = 14
输出：4

提示：

1 <= K <= 100
1 <= N <= 10000

代码参考：https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/

思路参考：https://leetcode-cn.com/problems/super-egg-drop/solution/ji-ben-dong-tai-gui-hua-jie-fa-by-labuladong/

"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(k,n):
            if (k,n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo,hi = 1,n
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k-1,x-1)

                        t2 = dp(k,n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    ans = 1 + min(max(dp(k-1,x-1),dp(k,n-x)) for x in (lo,hi))
                memo[k,n] = ans
            return memo[k,n]
        return dp(K,N)

if __name__ == '__main__':
    K = 3
    N = 14
    solution =  Solution()
    print(solution.superEggDrop(K,N))