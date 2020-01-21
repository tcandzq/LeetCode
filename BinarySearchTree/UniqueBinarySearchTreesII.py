# -*- coding: utf-8 -*-
# @File    : UniqueBinarySearchTreesII.py
# @Date    : 2020-01-20
# @Author  : tc
"""
题号 95 不同的二叉搜索树II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
在真实的面试中遇到过这道题？

卡特兰数问题

参考：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode/

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate_trees(start,end):
            if start > end:
                return [None,]

            all_trees = []
            for i in range(start,end+1):
                left_trees = generate_trees(start,i-1)

                right_trees = generate_trees(i+1,end)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
        return generate_trees(1,n) if n else []



if __name__ == '__main__':
    solution = Solution()
    print(solution.generateTrees(3))





