# -*- coding: utf-8 -*-
# @File    : DeepestLeavesSum.py
# @Date    : 2020-02-24
# @Author  : tc
"""
1302. 层数最深叶子节点的和
给你一棵二叉树，请你返回层数最深的叶子节点的和。



示例：



输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15


提示：

树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。

参考：https://leetcode-cn.com/problems/deepest-leaves-sum/solution/ceng-shu-zui-shen-xie-zi-jie-dian-de-he-by-leetc-2/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_dep = -1
        self.total = 0
    # dfs
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(root,dep):
            if not root:
                return
            if dep > self.max_dep:
                self.max_dep,self.total = dep,root.val
            elif dep == self.max_dep:
                self.total += root.val
            dfs(root.left,dep+1)
            dfs(root.right,dep+1)
        dfs(root,0)
        return self.total



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node4.left = node7
    node3.right = node6
    node6.right = node8

    solution = Solution()
    print(solution.deepestLeavesSum(node1))
