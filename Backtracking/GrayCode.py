"""
题号 89 格雷编码
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。

参考:https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/

"""
from typing import List

class Solution:
    # 错误解答
    def grayCode(self, n: int) -> List[int]:
        res = []
        def trace_back(tmp):
            if len(tmp) >= n:
                res.append(tmp)
                return
            trace_back(tmp + [0])
            trace_back(tmp + [1])
        trace_back([])
        return res

    # 正确答案
    def grayCode2(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):  # 倒叙排列
                res.append(head + res[j])
            head <<= 1 # head 往左移动一位
        return res


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.grayCode2(n))