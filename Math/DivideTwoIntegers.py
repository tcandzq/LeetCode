"""
题号 29 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

代码参考:https://leetcode-cn.com/problems/divide-two-integers/solution/xiao-xue-sheng-du-hui-de-lie-shu-shi-suan-chu-fa-b/
思路参考:https://leetcode-cn.com/problems/divide-two-integers/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-4/

我们每次减 1 次除数，我们其实可以每次减多次。比如 10 / 1 ，之前是 10 - 1 = 9，计数器加 1 变成 1，然后 9 - 1 = 8，计数器加 1 变成 2，
然后 8 - 1= 7，计数器加 1 变成 3，直至减到 0 < 1，我们结束了循环。我们其实可以翻倍减， 减完 1 ，减 2 ，再减 4 ，在减 8，
当然计数器也不能只加 1 了，减数是翻倍减的，所以计数器也会一直翻倍的加。这里肯定会遇到一个问题，
比如 10 - 1 = 9，9 - 2 = 7，7 - 4 = 3，3 - 8 = -5 < 1，它就走出了 while 循环。但是 3 本来还可以减 3 次 1，
所以我们只要再递归就可以了。再看 3 / 1 的商，然后把之前的计数器的值加上 3 / 1 的商就够了。

"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1 if dividend ^ divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            res += 1
            dividend -= divisor
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

    def divide2(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # 把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count  # 翻倍的加
                dividend -= divisor  # 翻倍的减
        if sign: result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1



if __name__ == '__main__':
    dividend = 10
    divisor = 3
    solution = Solution()
    print(solution.divide2(dividend,divisor))