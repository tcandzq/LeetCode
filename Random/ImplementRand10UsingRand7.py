# -*- coding: utf-8 -*-
# @File    : ImplementRand10UsingRand7.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号 470. 用 Rand7() 实现 Rand10()
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]

提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。


进阶:

rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?

核心思想:
1.构造一个包含1~10尽可能小的随机数范围;
2.使用拒绝采样，从大的随机数范围中捞出想要的随机数

参考1:https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/cong-pao-ying-bi-kai-shi-xun-xu-jian-jin-ba-zhe-da/

参考2:https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/cong-zui-ji-chu-de-jiang-qi-ru-he-zuo-dao-jun-yun-/

"""
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 40
        while rand40 >= 40:
            rand40 = (self.rand7() - 1) * 7 + self.rand7() - 1
        return rand40 % 10 + 1

    def rand7(self):
        pass