# -*- coding: utf-8 -*-
# @File    : AdvantageShuffle.py
# @Date    : 2022-06-20
# @Author  : tc
"""
870. 优势洗牌
给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。

示例 1：
输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]

示例 2：
输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
输出：[24,32,8,12]

如果 A 中最小的牌 a 能击败 B 中最小的牌 b，那么我们应当将它们配对。
否则， a 将无益于我们的比分，因为它无法击败任何牌。

我们为什么要在 a > b 时将 a 和 b 配对呢？
这是因为此时在 A 中的每张牌都比 b 要大，所以不管我们在 b 前面放置哪张牌都可以得分。
我们可以用手中最弱的牌来与 b 配对，这样会使 A 中剩余的牌严格地变大，因此会有更多得分点。

代码来自：https://leetcode.cn/problems/advantage-shuffle/solution/you-shi-xi-pai-by-leetcode/
"""
class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]