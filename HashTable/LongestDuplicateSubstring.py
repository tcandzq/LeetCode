# -*- coding: utf-8 -*-
# @File    : LongestDuplicateSubstring.py
# @Date    : 2020-02-26
# @Author  : tc
"""
题号 1044. 最长重复子串
给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。

返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）



示例 1：

输入："banana"
输出："ana"
示例 2：

输入："abcd"
输出：""


提示：

2 <= S.length <= 10^5
S 由小写英文字母组成。


参考1：https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode/
参考2：https://blog.csdn.net/lucylove3943/article/details/83491416

"""
from typing import List

class Solution:
    # 二分查找+滚动hash
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # 滚动哈希函数的底
        a = 26
        # 取模，防止出现溢出
        modulus = 2 ** 32

        # 二分搜索
        left,right = 0,n
        while left < right:
            L = left + (right - left) // 2
            if self.search(L,a,modulus,n,nums) != -1:
                left = L + 1
            else:
                right = L
        start = self.search(left - 1,a,modulus,n,nums)
        return S[start:start+left-1] if start != -1 else ""



    def search(self,L:int,a:int,modulus:int,n:int,nums:List[int]) -> int:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """

        # 计算字符串S[:L]的哈希值
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        seen = {h}
        aL = pow(a,L,modulus)  # a*L%modulus
        for start in range(1,n-L+1):
            # 使用O(1)时间复杂度 计算滚动hash
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1


    def longestDupSubstring2(self, S: str) -> str:
        from functools import reduce
        A = [ord(c)-ord('a') for c in S]
        mod = 2**63 - 1

        def search(L):
            p = pow(26,L,mod)
            cur = reduce(lambda x, y: (x*26+y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i-L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)
        res,lo,hi = 0,0,len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = search(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]



if __name__ == '__main__':
    s = "banana"
    solution = Solution()
    print(solution.longestDupSubstring2(s))