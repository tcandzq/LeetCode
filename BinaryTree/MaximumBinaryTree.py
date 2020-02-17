# -*- coding: utf-8 -*-
# @File    : MaximumBinaryTree.py
# @Date    : 2020-02-17
# @Author  : tc
"""
题号 654 最大二叉树
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

 

示例 ：

输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
 

提示：

给定的数组的大小在 [1, 1000] 之间。

1.递归终止条件?
当左子树和右子树的数组都为空时

2.本次递归做什么?
取出数组的最大值，并把数组根据最大值分成左右两个数组，然后进行递归赋值

3.返回什么?
子树的根节点


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root_index = nums.index(max(nums))
        root = TreeNode(max(nums))
        left = self.constructMaximumBinaryTree(nums[:root_index])
        right = self.constructMaximumBinaryTree(nums[root_index+1:])
        root.left = left
        root.right = right
        return root

if __name__ == '__main__':
    pass