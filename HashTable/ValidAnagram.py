"""
题号 242 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

"""
class Solution:
    # 解法1
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # 解法2(超时)
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            if s.count(char) != t.count(char):
                return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s,t))