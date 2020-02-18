# -*- coding: utf-8 -*-
# @File    : CompareVersionNumbers.py
# @Date    : 2020-02-18
# @Author  : tc
"""
题号 165 比较版本号
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
 

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1
示例 2:

输入: version1 = "1.0.1", version2 = "1"
输出: 1
示例 3:

输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
示例 4：

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
示例 5：

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
 

提示：

版本字符串由以点 （.） 分隔的数字字符串组成。这个数字字符串可能有前导零。
版本字符串不以点开始或结束，并且其中不会有两个连续的点。

简洁写法

"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        while version1 or version2:
            a = 0 if not version1 else int(version1.pop(0))
            b = 0 if not version2 else int(version2.pop(0))
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

    # 简洁写法
    def compareVersion2(self, version1: str, version2: str) -> int:
        from itertools import zip_longest
        v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
        v1, v2 = zip(*zip_longest(v1, v2, fillvalue=0))
        return (0, 1, -1)[(v1 > v2) - (v1 < v2)]

if __name__ == '__main__':
    version1 = "1.0"
    version2 = "1.0.0"
    solution = Solution()
    print(solution.compareVersion2(version1,version2))