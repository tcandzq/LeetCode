#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 9:20
# @Author  : tc
# @File    : HouseRobberIII.py
"""
题号 337 打家劫舍 III

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.


树形DP，第一次看到，记录一下

参考:https://leetcode-cn.com/problems/house-robber-iii/solution/shu-xing-dp-by-enda-2/

下面对 [max(left) + max(right), cur.val + left[0] + right[0]] 做详细的解释:
1.cur 表示根结点，left 表示左子树的结果，right表示右子树的结果，都是一个dp数组，其中dp[0]表示不使用根结点，dp[1]表示使用根结点；
2.当不使用根结点时，dp[0] = 左子树的最优值 + 右子树的最优值；
3.当使用根结点时，dp[1] = 根结点的值 + 左子树非根结点的最优值(即不使用左子树的根结点) + 右子树非根结点的最优值(即不使用右子树的根结点)

树形DP = 树形(后序遍历) + DP(dp数组，dp[0]表示不使用根结点的状态，dp[1]表示使用根结点的状态)

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))

    def dp(self, cur: TreeNode) -> List[int]:
        if not cur:
            return [0, 0]

        left = self.dp(cur.left)
        right = self.dp(cur.right)

        return [max(left) + max(right), cur.val + left[0] + right[0]]


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.right = node5

    solution = Solution()
    print(solution.rob(node1))
