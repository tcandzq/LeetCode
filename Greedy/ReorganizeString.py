# -*- coding: utf-8 -*-
# @File    : ReorganizeString.py
# @Date    : 2022-08-14
# @Author  : tc
"""
767. 重构字符串
给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。

返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。
示例 1:

输入: s = "aab"
输出: "aba"
示例 2:

输入: s = "aaab"
输出: ""
提示:

1 <= s.length <= 500
s 只包含小写字母

基于最大堆的贪心

维护最大堆存储字母，堆顶元素为出现次数最多的字母。首先统计每个字母的出现次数，然后将出现次数大于 00 的字母加入最大堆。
当最大堆的元素个数大于1时，每次从最大堆取出两个字母，拼接到重构的字符串，然后将两个字母的出现次数分别减1，
并将剩余出现次数大于0的字母重新加入最大堆。由于最大堆中的元素都是不同的，因此取出的两个字母一定也是不同的，
将两个不同的字母拼接到重构的字符串，可以确保相邻的字母都不相同。
如果最大堆变成空，则已经完成字符串的重构。如果最大堆剩下 11 个元素，则取出最后一个字母，拼接到重构的字符串。

参考:https://leetcode.cn/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode-solution/
"""
import collections
import heapq
class Solution:
	def reorganizeString(self, s: str) -> str:
		if len(s) < 2:
			return s

		length = len(s)
		counts = collections.Counter(s)
		maxCount = max(counts.items(), key = lambda x:x[1])[1]
		if maxCount > (length + 1) // 2:
			return ""

		queue = [(-x[1], x[0]) for x in counts.items()]
		heapq.heapify(queue)
		ans = list()

		while len(queue) > 1:
			_, letter1 = heapq.heappop(queue)
			_, letter2 = heapq.heappop(queue)

			ans.extend([letter1, letter2])
			counts[letter1] -= 1
			counts[letter2] -= 1
			if counts[letter1] > 0:
				heapq.heappush(queue, (-counts[letter1], letter1))

			if counts[letter2] > 0:
				heapq.heappush(queue, (-counts[letter2], letter2))

		if queue:
			ans.append(queue[0][-1])
		return "".join(ans)