"""
题号 448 找到所有数组中消失的数字
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

抽屉原理，即一个萝卜一个坑
参考:https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/tong-pai-xu-ji-yu-yi-huo-yun-suan-jiao-huan-liang-/

"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def swap(nums,index1,index2):
            if index1 == index2:
                return
            nums[index1] = nums[index1] ^ nums[index2]
            nums[index2] = nums[index1] ^ nums[index2]
            nums[index1] = nums[index1] ^ nums[index2]

        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                swap(nums,i,nums[i] - 1)
        print(nums)
        return [i + 1 for i, num in enumerate(nums) if num != i + 1]

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    print(solution.findDisappearedNumbers(nums))
