"""
题号 171 Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

这个问题实际是将26进制转为10进制

参考：https://leetcode-cn.com/problems/excel-sheet-column-number/solution/26jin-zhi-zhuan-shi-jin-zhi-by-powcai/

"""
class Solution:
    # 丑陋版
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1,-1,-1):
            ans += (ord(s[-(1+i)]) - ord('A') + 1) * (26 ** i)
        return ans

    # 优雅版
    def titleToNumber2(self, s: str) -> int:
        # 26进制转10进制
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x) - ord('A') + 1
        return ans

if __name__ == '__main__':
    s = "ZY"
    solution = Solution()
    print(solution.titleToNumber(s))
