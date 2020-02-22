# -*- coding: utf-8 -*-
# @File    : MaximumXorOfTwoNumbersInAnArray.py
# @Date    : 2020-02-22
# @Author  : tc
"""
题号 421. 数组中两个数的最大异或值
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

示例:

输入: [3, 10, 5, 25, 2, 8]

输出: 28

解释: 最大的结果是 5 ^ 25 = 28.


思路参考：https://blog.csdn.net/qq_41855420/article/details/88756998

代码参考：https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/130522/python-trie-solution-O(n)

"""
from typing import List

class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    # 超时
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        max_xor = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] ^ nums[j] > max_xor:
                    max_xor = nums[i] ^ nums[j]
        return max_xor

    # 构建字典树
    def findMaximumXOR2(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            node = root
            #  按照[31,30, .... 1，0]二进制数字串的位位0、1进行区别，1放左边，0放右边
            #  从高位向低位逐渐检测，递归寻找放的位置
            for j in range(31,-1,-1):
                temp = num & (1 << j)
                # num的第i位为1，需要放到当前节点的1节点处
                if temp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one  # 转移到1节点，进行i + 1的放置
                # num的第i位为0，需要放到当前节点的0节点
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero  # 转移到0节点，进行i + 1的放置

        ans = 0
        for num in nums:
            node = root
            temp_val = 0
            # 从高位向低位寻找，贪心策略，尽量保持当前位异或为1
            for j in range(31,-1,-1):
                temp = num & 1 << j
                if node.one and node.zero:
                    # 如果此位是1，则应该优先选择0节点
                    if temp:
                        node = node.zero
                    # 如果num的第i位0，则应该优先选择1节点，因为right为1，这样1 ^ 0 == 1
                    else:
                        node = node.one
                    temp_val += 1 << j
                else:
                    if (node.zero and temp) or (node.one and not temp):
                        temp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans,temp_val)
        return ans





if __name__ == '__main__':
    # nums = [3, 10, 5, 25, 2, 8]
    # solution = Solution()
    # print(solution.findMaximumXOR2(nums))
    num = 3
    temp = 0
    print(3 & 4294967296)
    print(1 << 32)
    # for i in range(31,-1,-1):
    #     temp = num & 1 << i
    #     print(temp)
