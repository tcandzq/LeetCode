# -*- coding: utf-8 -*-
# @File    : OpenTheLock.py
# @Date    : 2022-06-20
# @Author  : tc
"""
752. 打开转盘锁
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。


示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

示例 2:
输入: deadends = ["8888"], target = "0009"
输出：1
解释：把最后一位反向旋转一次即可 "0000" -> "0009"。

示例 3:
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：无法旋转到目标数字且不被锁定。
"""
from typing import List,Generator
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        def num_prev(x: str) -> str:
            return "9" if x == "0" else str(int(x) - 1)

        def num_succ(x: str) -> str:
            return "0" if x == "9" else str(int(x) + 1)

        # 枚举 status 通过一次旋转得到的数字
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i] = num_prev(num)
                yield "".join(s)
                s[i] = num_succ(num)
                yield "".join(s)
                s[i] = num

        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                print(next_status)
                if next_status not in seen and next_status not in dead:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)

        return -1
