# -*- coding: utf-8 -*-
# @File    : ValidateBinaryTreeNodes.py
# @Date    : 2020-02-27
# @Author  : tc
"""
题号 1361. 验证二叉树
二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。

只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。

注意：节点没有值，本问题中仅仅使用节点编号。



示例 1：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true
示例 2：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false
示例 3：



输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false
示例 4：



输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
输出：false


提示：

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1

一棵二叉树需要满足以下要求：

    1.一个顶点的出度最多为2，入度最多为1

    2.只有一个根节点，即有且只有一个节点的入度为0

"""
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degrees,out_degrees = [0] * n, [0] * n

        for i in range(n):
            if leftChild[i] != -1:
                in_degrees[leftChild[i]] += 1
                out_degrees[i] += 1
            if rightChild[i] != -1:
                in_degrees[rightChild[i]] += 1
                out_degrees[i] += 1

        for i in range(n):
            if in_degrees[i] > 1 or out_degrees[i] > 2:
                return False
        if in_degrees.count(0) != 1:
            return False
        return True


if __name__ == '__main__':
    n = 4
    leftChild = [1,-1,3,-1]
    rightChild = [2,3,-1,-1]
    solution = Solution()
    print(solution.validateBinaryTreeNodes(n,leftChild,rightChild))




