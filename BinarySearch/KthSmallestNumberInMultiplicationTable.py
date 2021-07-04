# -*- coding: utf-8 -*-
# @File    : KthSmallestNumberInMultiplicationTable.py
# @Date    : 2021-07-05
# @Author  : tc
"""
题号 668. 乘法表中第k小的数
几乎每一个人都用乘法表。但是你能在乘法表中快速找到第k小的数字吗？

给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：

输入: m = 3, n = 3, k = 5
输出: 3
解释:
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
例 2：

输入: m = 2, n = 3, k = 6
输出: 6
解释:
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).

这道题可能有人会想着先构造出这个乘法表，然后再去搜索，但这样是行不通的，
因为m、n的取值可能非常大，非常耗内存。首先我们知道在m、n的乘法表中取值范围为[1, m * n]，
那么我们可不可以使用使用二分搜索呢？

首先观察乘法表我们会发现，由于构造关系，决定了他每一行都是递增的。

如果我们需要在第i行中寻找大于num的个数，我们只要min(num / i, n)，
其中（i是这一行的行号，n是矩阵的列数）num / i代表的是如果num也在第i行，
它存在的列数，所以只要取最小值就是第i行不大于num的个数。
（比如例题1中，我们需要知道第2行，不大于4的个数，min(4 / 2, 3) == 2个（就是2， 4））

那么如果我们需要确定这个乘法表中不大于num的个数就非常简单了，我们只要将每一行
不大于num的个数累加即可。（比如例题1中，我们需要知道乘法表中不大于4的个数，
第一行3个、第二行2个，第三行1个）

现在我们就可以使用二分搜索了，初始化left = 1， right = n * m + 1，
mid = （left + right） / 2，在m，n的乘法表中寻找不超过mid的个数。

参考:https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/106984/Python-Straightforward-with-Explanation

"""
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            return sum(min(x // i, n) for i in range(1, m+1)) # 记录乘法表中所有不大于m的值的数量
        lo = 1
        hi = m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if enough(mi) < k: # 如果不大于m的数量小于k,也就是m偏小(理解为有序数组中m的索引小于k)
                lo = mi + 1
            else:
                hi = mi # 如果不大于m的数量大于等于k,也就是m偏大(理解为有序数组中m的索引大于k)
        return lo