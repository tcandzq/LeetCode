"""
题号 118 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows: return []
        res = [[1]]
        for i in range(numRows-1):
            tmp = [1]
            nums = res[i]
            for j in range(len(nums)-1):
                tmp.append(nums[j] + nums[j+1])
            res.append(tmp+[1])
        return res

if __name__ == '__main__':
    numRows = 5
    solution = Solution()
    print(solution.generate(numRows))