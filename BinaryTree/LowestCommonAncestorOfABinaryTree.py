#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 22:35
# @Author  : tc
# @File    : LowestCommonAncestorOfABinaryTree.py
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

完全不会写,不过参考答案的代码也太6了吧
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-di-gui-jie-fa-si-xing-dai-ma-by-sunshy/

真是把递归用的炉火纯青,因为两个结点的最近公共祖先一定是一棵包含了这两个结点的最小二叉树,那只要返回对应的结点就行了。

两个节点p,q分为两种情况：

p和q在相同子树中
p和q在不同子树中
从根节点遍历，递归向左右子树查询节点信息
递归终止条件：如果当前节点为空或等于p或q，则返回当前节点

递归遍历左右子树，如果左右子树查到节点都不为空，则表明p和q分别在左右子树中，因此，当前节点即为最近公共祖先；
如果左右子树其中一个不为空，则返回非空节点。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    if not root or root == p or root == q:  # 递归的边界条件是关键
        return root
    left = lowestCommonAncestor(root.left,p,q)  # 遍历左子树查找
    right = lowestCommonAncestor(root.right,p,q)  # 遍历右子树查找
    if not left:
        return right
    elif not right:
        return left
    else:  # 如果p和q分别在左右子树中则返回左右字数的根结点
        return root

if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(0)
    node6 = TreeNode(8)
    node7 = TreeNode(7)
    node8 = TreeNode(4)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left= node5
    node2.right = node6
    node4.left = node7
    node4.right = node4

    print(lowestCommonAncestor(root,node1,node2).val)
