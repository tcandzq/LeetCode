# -*- coding: utf-8 -*-
# @File    : MinimumRemoveToMakeValidParentheses.py
# @Date    : 2020-02-24
# @Author  : tc
"""
题号 1249. 移除无效的括号
给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」


示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
示例 2：

输入：s = "a)b(c)d"
输出："ab(c)d"
示例 3：

输入：s = "))(("
输出：""
解释：空字符串也是有效的
示例 4：

输入：s = "(a(b(c)d)"
输出："a(b(c)d)"


提示：

1 <= s.length <= 10^5
s[i] 可能是 '('、')' 或英文小写字母

参考：https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/503754/Python-Memory-Usage-Less-Than-100-Faster-than-100

"""
class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        s = list(s)

        for i,c in enumerate(s):
            if c == '(':
                open += 1
            elif c == ')':
                if not open:
                    s[i] = ""
                else:
                    open -= 1
        for i in range(len(s)):  # 注意这里要倒序否则会  "())()((("  -> "))(("。因为第一轮正序保证了前面一个'('对应一个'c'
                                # 如果 open 大于0 那么说明有很多字符串的后面有很多'('没有被消去，所以从后往前遍历
            print(i)
            if not open:
                break
            if s[i] == '(':
                s[i] = ""
                open -= 1
        return "".join(s)

    def minRemoveToMakeValid2(self, s: str) -> str:
        s = list(s)
        n = len(s)
        stack = []
        g = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    g.append(i)
        if stack:
            for index in stack:
                s[index] = ''
        if g:
            for index in g:
                s[index] = ''

        return ''.join(s)


if __name__ == '__main__':
    s = "())()((("
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))