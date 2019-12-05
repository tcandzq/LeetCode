"""
题号 44 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

dp[i][j]：字符串以s[i]结尾和p[j]结尾的字符串是否匹配

当 * 起空串作用时相当于p的第j个位置的字符不存在，毫无意义，则dp[i][j] = dp[i][j-1],

当* 起任意字符串时相当于s的第i个位置的字符可以被p[j]任意匹配，则dp[i][j] = dp[i-1][j]

参考:https://leetcode-cn.com/problems/wildcard-matching/solution/shuang-zhi-zhen-he-dong-tai-gui-hua-by-powcai/

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)] # 初始化的时候注意下，行是s，列是p，下面的dp过程已经很暗示了
        dp[0][0] = True
        for k in range(1, len(p)+1):
            if p[k - 1] == '*':
                dp[0][k] = dp[0][k-1]
        for i in range(1, len(s)+1):
            for j in range(1,len(p)+1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j -1] == '?':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i-1][j]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
        return dp[len(s)][len(p)]

if __name__ == '__main__':
    s = "aa"
    p = "*"
    solution = Solution()
    print(solution.isMatch(s,p))