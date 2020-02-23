""""
题号 127 单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

参考:https://leetcode-cn.com/problems/word-ladder/solution/bfscong-wu-dao-you-by-powcai/

"""
from typing import List

class Solution:
    # BFS解法
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        visited = set()

        # 看两个单词是否差一个字母
        def is_one_letter(w, word):
            if len(w) != len(word):
                return False
            dif = 0
            for i in range(len(w)):
                if w[i] != word[i]: dif += 1
                if dif > 1: return False
            return True

        # 发现所有和word相差一个字母的单词
        def find_only_one_letter(word):
            ans = []
            for w in wordList:
                # print(is_one_letter(w, word))
                if w not in visited and is_one_letter(w, word):
                    ans.append(w)
            # print(ans)
            return ans

        queue = deque()
        queue.appendleft(beginWord)
        res = 1
        # BFS
        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if tmp == endWord:
                    return res
                visited.add(tmp)
                for t in find_only_one_letter(tmp):
                    queue.appendleft(t)
            res += 1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordict = set(wordList)
        s1 = {beginWord}
        s2 = {endWord}
        n = len(beginWord)
        step = 0
        wordict.remove(endWord)
        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            for word in s1:
                nextword = [word[:i] + chr(j) + word[i + 1:] for j in range(97, 123) for i in range(n)]
                for w in nextword:
                    if w in s2:
                        return step + 1
                    if w not in wordict:
                        continue
                    wordict.remove(w)
                    s.add(w)
            s1 = s
        return 0

    # 标准写法
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import collections
        import string
        arr = set(wordList)
        q = collections.deque([(beginWord,1)])
        visited = set()
        alpha = string.ascii_lowercase
        while q:
            word,length = q.popleft()
            # 为什么是queue，而不是stack，因为先进来的字符找到继任者后就要排除，下一个选项是根据新找到的字所衍生的，而不是根据最早的
            if word == endWord:
                return length
            for i in range(len(word)):
                # hit -> *it 或 h*t 或 hi*
                for ch in alpha:
                    # aloha 中含有abcd...z，每个字母都换换看
                    new_word = word[:i] + ch + word[i+1:]
                    #
                    if new_word in arr and new_word not in visited:
                        # 如果该字符串在字典里面，且该新字符没有被访问过，则加入
                        q.append((new_word,length+1))
                        visited.add(new_word)
        return 0



if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    print(solution.ladderLength(beginWord,endWord,wordList))
