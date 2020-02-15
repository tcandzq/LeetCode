# -*- coding: utf-8 -*-
# @File    : DeleteNodeInABst.py
# @Date    : 2020-02-15
# @Author  : tc
"""
题号 450 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

参考1：https://leetcode.com/problems/delete-node-in-a-bst/discuss/93374/Simple-Python-Solution-With-Explanation
参考2：https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/yong-qian-qu-huo-zhe-hou-ji-jie-dian-zi-shu-dai-ti/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val > key:   # key位于左子树
            root.left = self.deleteNode(root.left,key)
        # 注意：写成if 会出现错误
        elif root.val < key:  # key位于右子树
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:  # 如果 它没有左子树，那就用右子树作为root
                return root.right
            if not root.right:  # 如果 它没有右子树，那就用左子树作为root
                return root.left
            # 如果左右子树都存在，那就用右子树的最小值替代它，然后删掉右子树最小值的那个节点
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini  # 替换该值
            root.right = self.deleteNode(root.right,mini)  # 删除掉右子树中的最小值节点
        return root

if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(6)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(7)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5

    solution = Solution()
    key = 3
    print(solution.deleteNode(root,key))

