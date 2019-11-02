#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 16:48
# @Author  : tc
# @File    : SumRootToLeafNumbers.py
"""
题号 129 求根到叶子节点数字之和

给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

回溯解法：一看就是二叉树的先序遍历，用递归函数的入参来存储递归过程的中间变量，用叶子结点作为递归的另外一个边界条件


简洁解法1：对"冗余解法"的改进，直接在DFS过程中计算res，更加彻底。

简洁解法2：res = res * 10 另外这个解法的代码要熟记，很有意思，细节值得反复推敲。
参考:https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-3-5/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #  冗余的解法
    def sumNumbers(self, root: TreeNode) -> int:
        sum_numbers = 0
        res = []

        def helper(root,tmp_list):
            if not root:
                return
            if not root.left and not root.right:
                # tmp_list += [root.val]
                res.append(tmp_list)
            helper(root.left,tmp_list+[root.val])
            helper(root.right, tmp_list + [root.val])
        helper(root,[])
        for nums in res:
            sum_numbers += self.get_number(nums)
        return sum_numbers

    def get_number(self,nums):
        number = 0
        size = len(nums)
        for index in range(size):
            number += nums[index] * (10 ** (size- 1 - index))
        return number


    # 简洁解法1(用字符串存储中间变量)
    def sumNumbers2(self, root: TreeNode) -> int:
        if not root: return 0
        res = []

        def dfs(node, tmp, res):
            if not node:
                return  # 当树中的节点出现只有左子树或右子树的情况，这一句保证下一句不出错。
            if not node.left and not node.right:  # 判断当前结点是否为叶子结点，是的话返回值，加入到res列表中
                res.append(int(tmp + str(node.val)))
                return
            tmp += str(node.val)
            dfs(node.left, tmp, res)
            dfs(node.right, tmp, res)

        dfs(root, '', res)
        return sum(res)

    _sum = 0  # 这种在类中保存全局变量的方式也很有技巧
    # 简洁解法3 这个解法很有意思
    def sumNumbers3(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root,current_sum):
            if not root:
                return
            if not root.left and not root.right:
                self._sum += current_sum  # 注意这里不需要像解法1那样再做一次current_sum *10+ root.val
                return

            dfs(root.left, current_sum * 10 + root.left.val) # 注意是root.left.val 不是root.val.

            dfs(root.right, current_sum * 10 + root.right.val)

        dfs(root, root.val)  # 注意这里不是dfs(root,0) 考虑下为什么？
        return self._sum


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(9)
    node3 = TreeNode(0)
    node4 = TreeNode(5)
    node5 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    solution = Solution()
    print(solution.sumNumbers3(node1))