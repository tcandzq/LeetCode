# -*- coding: utf-8 -*-
# @File    : EussianDollEnvelopes.py
# @Date    : 2020-02-12
# @Author  : tc

"""
题号 354 俄罗斯套娃信封问题
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

本题的核心是LIS(最长上升子序列)问题但有几点需要注意：

1.由于信封的宽和高都要比另外一个信封的宽和高大，所以可以先对宽升序，再对高降序，这样做的原因：
如果两个信封的宽是一样的，且按照升序排列，那么再对高做LIS的时候，这两个信封都有可能被选中，这样就违背了题目的要求。
参考:https://leetcode-cn.com/problems/russian-doll-envelopes/solution/tan-xin-suan-fa-er-fen-cha-zhao-python-dai-ma-java/

2.动态规划求解会超时间，时间复杂度为O(N*N)，可以使用贪心+二分查找，时间复杂度为O(logN*N)

"""
from typing import List

class Solution:
    # 动态规划(超时)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes = sorted(envelopes,key=lambda x: (x[0],-x[1]))
        n = len(envelopes)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j] + 1,dp[i])
        return max(dp)

    # 贪心+二分查找
    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        size = len(envelopes)
        if size < 2:
            return size
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        tail = [envelopes[0][1]]
        for i in range(1,size):
            target = envelopes[i][1]
            if target > tail[-1]:
                tail.append(target)
                continue
            left,right = 0,len(tail)
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = target
        return len(tail)

if __name__ == '__main__':
    envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
    solution = Solution()
    print(solution.maxEnvelopes2(envelopes))