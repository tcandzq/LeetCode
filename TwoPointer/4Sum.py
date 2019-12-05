"""
题号 18 四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

在三数之和的基础上再加个for循环，即四指针:

参考:https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/

"""
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []
        for a in range(len(nums) -3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums) - 2):
                if b > a+1 and nums[b] == nums[b -1]:
                    continue
                i,j = b + 1, len(nums) - 1
                while i < j:
                    s = nums[a] + nums[b] + nums[i] + nums[j]
                    if s < target:
                        i += 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                    elif s > target:
                        j -= 1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
                    else:
                        ans.append([nums[a], nums[b], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i -1]:
                            i += 1
                        while i < j and nums[j] == nums[j +1]:
                            j -= 1
        return ans

if __name__ == '__main__':
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    solution = Solution()
    print(solution.fourSum(nums,target))