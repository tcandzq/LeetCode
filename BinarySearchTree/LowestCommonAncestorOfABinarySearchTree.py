#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 13:40
# @Author  : tc
# @File    : LowestCommonAncestorOfABinarySearchTree.py
"""
题号 235 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

参考:https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian--2/

极简解法参考:https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/python-2xing-by-knifezhu-3/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parent_val = root.val

        p_val = p.val

        q_val = q.val

        if p_val > parent_val and q_val > parent_val:  # 如果节点 p 和节点 q 都在右子树上
            return self.lowestCommonAncestor(root.right, p, q)

        elif p_val < parent_val and q_val < parent_val: # 如果节点 p 和节点 q 都在左子树上
            return self.lowestCommonAncestor(root.left, p, q)

        else:  #  如果  p < root < q
            return root


    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root



if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node6.left = node2
    node6.right = node8
    node2.left = node0
    node2.right = node4
    node8.left = node7
    node8.right = node9
    node4.left =node3
    node4.right = node5

    solution = Solution()
    p = node2
    q = node8
    print(solution.lowestCommonAncestor(node6,p,q))