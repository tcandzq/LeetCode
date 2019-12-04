"""
题号 387 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from _collections import OrderedDict
        order_dict = OrderedDict(s)
        for char in s:
            if char not in order_dict:
                order_dict[char] = 1
            else:
                order_dict[char] += 1
        for key,val in order_dict.items():
            if val == 1:
                return s.index(key)
        return -1

    # 使用collections.Counter()很巧妙
    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        import collections
        count = collections.Counter(s)

        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1
        return -1


if __name__ == '__main__':
    s = "loveleetcode"
    solution = Solution()
    print(solution.firstUniqChar(s))