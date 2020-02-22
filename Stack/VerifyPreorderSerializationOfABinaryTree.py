# -*- coding: utf-8 -*-
# @File    : VerifyPreorderSerializationOfABinaryTree.py
# @Date    : 2020-02-22
# @Author  : tc
"""
题号 331 验证二叉树的前序序列化

序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
示例 2:

输入: "1,#"
输出: false
示例 3:

输入: "9,#,#,1"
输出: false

非空节点占据一个槽位，但会创建两个新的槽位，空节点只会占据一个槽位

参考：https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78564/The-simplest-python-solution-with-explanation-(no-stack-no-recursion)

"""
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        p = preorder.split(',')
        # 初始化一个空槽位放置根节点
        slot = 1
        for node in p:
            # 没有空槽位放置当前节点
            if slot == 0:
                return False
            # 空节点占据一个槽位
            if node == '#':
                slot -= 1
            else:
                slot += 1  # 空节点占一个槽位，产生2个槽位，净得1个槽位
        return slot == 0

if __name__ == '__main__':
    pass