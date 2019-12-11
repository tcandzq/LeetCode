"""
题号 541 反转字符串II
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。

参考:https://leetcode-cn.com/problems/reverse-string-ii/solution/fan-zhuan-zi-fu-chuan-ii-by-leetcode/

"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2 * k  # 初始化左中右指针
        res = ''  # 初始化结果字符串
        while len(res) < len(s):  # 满足条件时执行
            res += s[left:mid][::-1] + s[mid:right]  # 把当前单元的结果添加到结果字符串
            left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k
        return res  # 返回结果

    # 解法2
    def reverseStr2(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)


if __name__ == '__main__':
    s = "a"
    k = 2
    solution = Solution()
    print(solution.reverseStr2(s,k))
