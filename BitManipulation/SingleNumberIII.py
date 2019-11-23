#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 17:58
# @Author  : tc
# @File    : SingleNumberIII.py
"""
题号 260 只出现一次的数字III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

牢记low bit运算以及异或运算的性质

参考1:https://leetcode-cn.com/problems/single-number-iii/solution/zhi-chu-xian-yi-ci-de-shu-zi-iiixiang-jie-pai-xu-h/
参考2:https://leetcode-cn.com/problems/single-number-iii/solution/cai-yong-fen-zhi-de-si-xiang-jiang-wen-ti-jiang-we/

"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = 0
        for num in nums:  # 把所有的元素进行异或操作，最终得到一个异或值。因为是不同的两个数字，所以这个值必定不为0；
            res ^= num
        n = res & (-res)  # low bit运算 取异或值最后一个二进制位为1的数字作为mask，如果是1则表示两个数字在这一位上不同。
        a, b = 0, 0
        for num in nums:
            if num & n == 0:  # 注意这里千万不能写1,因为n一定是1,2,4,8等,因此num & n的结果只有两大类情况即0和n
                a ^= num
            else:
                b ^= num
        return b, a

if __name__ == '__main__':
    nums = [1,2,1,3,2,5]
    solution = Solution()
    print(solution.singleNumber(nums))