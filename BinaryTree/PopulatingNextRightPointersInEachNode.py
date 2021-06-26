# -*- coding: utf-8 -*-
# @File    : PopulatingNextRightPointersInEachNode.py
# @Date    : 2021-06-26
# @Author  : tc
"""
题号 116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

二叉树的层序遍历

https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/

"""
class Solution(object):
	def connect(self, root):
		if not root:
			return root
		pre = root
		# 循环条件是当前节点的left不为空，当只有根节点
		# 或所有叶子节点都出串联完后循环就退出了
		while pre.left:
			tmp = pre
			while tmp:
				# 将tmp的左右节点都串联起来
				# 注:外层循环已经判断了当前节点的left不为空
				tmp.left.next = tmp.right
				# 下一个不为空说明上一层已经帮我们完成串联了
				if tmp.next:
					tmp.right.next = tmp.next.left
				# 继续右边遍历
				tmp = tmp.next
			# 从下一层的最左边开始遍历
			pre = pre.left
		return root

