#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 21:36
# @Author  : tc
# @File    : NumberOfDigitOne.py
"""
题号 233 数字1的个数
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

思考:

对于n=12，可以拆分为01~09,10~12，即 f(12) = f(10 - 1) + f(12 - 10) + 3,其中3是表示最高位为1的数字个数，这里就是10,11,12；

对于n=132，可以拆分为0~99，100~132，即f(132)=f(100 -1) + f(132 - 100) + 33，33代表最高位为1的数字的个数，这里就是100~132百位数字的1出新了33次

对于232，可以拆分为0~99，100~232，即f(232) = 2*f(100 - 1) + f(32) + 100，因为232大于199，所以它包括了所有最高位为1的数字即100~199，共100个。

参考1:https://leetcode-cn.com/problems/number-of-digit-one/solution/wo-men-ke-yi-jiang-yi-ge-shu-zi-chai-fen-wei-zui-g/

参考2:https://blog.csdn.net/gatieme/article/details/51292339

"""
class Solution:
    # 超时解法
    def countDigitOne(self, n: int) -> int:
        count = 0
        for num in range(1,n+1):
            if num < 10:
                if num == 1:
                    count += 1
            else:
                while num > 0:
                    reside = num % 10
                    if reside == 1:
                        count += 1
                    num = int(num / 10)

        return count

    # 递归解法
    def countDigitOne2(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        last = int(str(n)[1:])
        high = int(str(n)[0])
        power = 10 ** (len(str(n)) - 1)
        if high == 1:
            return self.countDigitOne(last) + self.countDigitOne(power - 1) + last + 1
        else:
            return power + high * self.countDigitOne(power - 1) + self.countDigitOne(last)

    # 数位dp解法
    def countDigitOne3(self, n: int) -> int:
        return self.solve(n)

    memo = [[]]
    digit = []

    def solve(self, n):
        self.digit = [0] * 64
        length = 0
        while n:
            length += 1
            self.digit[length] = n % 10 if n > 0 else n % -10
            n = int(n / 10)
        self.memo = [[-1] * (length+1) for _ in range(length)]
        return self.dfs(length,0,1,1)

    def dfs(self,pos,sm,lead,limit):
        if pos == 0:
            return sm
        if not lead and not limit and self.memo[pos][sm] != -1:
            return self.memo[pos][sm]
        up = self.digit[pos] if limit else 9
        ret = 0
        for i in range(up+1):
            ret += self.dfs(pos-1, sm + (i == 1),lead and (i == 0),limit and (i == up))
        if not limit and not lead:
            self.memo[pos][sm] = ret
        return ret





if __name__ == '__main__':
    n = 54321
    solution = Solution()
    print(solution.countDigitOne3(n))