# -*- coding: utf-8 -*-
# @File    : OnesAndZeroes.py
# @Date    : 2020-02-13
# @Author  : tc
"""
题号 474 一和零
在计算机界中，我们总是追求用有限的资源获取最大的收益。

现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。

你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

注意:

给定 0 和 1 的数量都不会超过 100。
给定字符串数组的长度不会超过 600。
示例 1:

输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
输出: 4

解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
示例 2:

输入: Array = {"10", "0", "1"}, m = 1, n = 1
输出: 2

解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。

思路：把总共的 0 个 1 的个数视为背包的容量，每一个字符串视为装进背包的物品。这道题就可以使用 0-1 背包问题的思路完成。这里的目标值是能放进背包的字符串的数量。

参考：https://leetcode-cn.com/problems/ones-and-zeroes/solution/dong-tai-gui-hua-zhuan-huan-wei-0-1-bei-bao-wen-ti/

"""
from typing import List

class Solution:
    # 01背包问题空间优化版
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def calc_zero_and_one(s):
            cnt = [0] * 2
            for c in s:
                cnt[int(c)] += 1
            return cnt

        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            cnt = calc_zero_and_one(s)
            for i in range(m,-1,-1):  # 注意要逆序
                for j in range(n,-1,-1): # 注意到逆序
                    if i-cnt[0] >= 0 and j-cnt[1] >= 0:
                        dp[i][j] = max(dp[i][j],dp[i-cnt[0]][j-cnt[1]]+1)
        return dp[m][n]




if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    solution = Solution()
    print(solution.findMaxForm(strs,m,n))