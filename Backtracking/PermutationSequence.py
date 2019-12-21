# -*- coding: utf-8 -*-
# @File    : PermutationSequence.py
# @Date    : 2019-12-21
# @Author  : tc
"""
题号 60 第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

这题的关键是如何合理剪枝

这题基本的思路是利用回溯法在回溯到第k个排列时终止，但这种终止实际上是不能提前跳出的，所以最好的方法是进行剪枝。

这题的剪枝起到了提前终止的目的：
1.在选择路径的时候进行剪枝，在for循环里面使用continue 这样每次该结点下的所有分支都会被剪掉；
2.当k -= 0时，回溯函数在某一个特定的分支下调用了，前当k - 1次的分支全部都被剪掉了，这也是为什么代码中used[i]无需回溯，设置
used[i] = False的原因。因为回溯只需要完整的走完一个分支，到达该该分支的叶子结点即可。

这样代码整体上就起到了回溯在第k次时提前跳出的效果，但实际上是前k-1次都是剪枝。

"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return ''
        nums = [i + 1 for i in range(n)]
        used = [False for _ in range(n)]

        return self.__dfs(nums, used, n, k, 0, [])

    def __factorial(self, n):
        # 这种编码方式包括了 0 的阶乘是 1 这种情况
        res = 1
        while n:
            res *= n
            n -= 1
        return res

    def __dfs(self, nums, used, n, k, depth, pre):
        if depth == n:
            # 在叶子结点处结算
            return ''.join(pre)
        # 后面的数的全排列的个数
        ps = self.__factorial(n - 1 - depth)
        print(ps)
        for i in range(n):
            # 如果这个数用过，就不再考虑
            if used[i]:
                continue
            # 后面的数的全排列的个数小于 k 的时候，执行剪枝操作
            if ps < k:
                k -= ps
                continue
            pre.append(str(nums[i]))
            # 因为直接走到叶子结点，因此状态不用恢复
            used[i] = True
            return self.__dfs(nums, used, n, k, depth + 1, pre)


if __name__ == '__main__':
    n = 4
    k = 9
    solution = Solution()
    print(solution.getPermutation(n,k))