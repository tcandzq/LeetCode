# -*- coding: utf-8 -*-
# @File    : MonotoneIncreasingDigits.py
# @Date    : 2022-06-21
# @Author  : tc
"""
738. 单调递增的数字
当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

示例 1:
输入: n = 10
输出: 9

示例 2:
输入: n = 1234
输出: 1234

示例 3:
输入: n = 332
输出: 299

这是一道很明显的贪心题目。既然要尽可能的大，那么这个数从高位开始要尽可能地保持不变。那么我们找到从高到低第一个满足 str[i]>str[i+1] 的位置，
然后把 str[i]−1，再把后面的位置都变成 9 即可。对应可看下面的例子。

n   = 1234321
res = 1233999

但是由于减小了 str[i]str[i] 以后，可能不满足 str[i-1] <= str[i]str[i−1]<=str[i] 了，所以我们在分析下这种情况怎么处理。我们看下这种情况的例子：

n    = 2333332
res  = 2299999

下面这段比较啰嗦，其实你看了上面的例子你就知道怎么写了。
注意到如果减小 str[i]以后不满足str[i−1]<=str[i]，那么肯定有 str[i−1]==str[i]，此时就需要再str[i−1]−1，
递归地会处理到某个位置 idx，我们发现 str[idx]==str[idx+1]==...=str[i] 。然后只要str[idx]−1，然后后面都补上9即可。

所以代码写起来很简单了。遍历各位数字的时候，求当前最大的数字 max。然后只在max<arr[i] 的时候才更新 max 对应的 idx
（写法类似于查找数组中最大的元素，返回最小的下标）。接着判断是否有arr[i]>arr[i+1]，如果是，那么 idx 位置数字减 1，
后面的位置全部置9即可。

https://leetcode.cn/problems/monotone-increasing-digits/solution/jian-dan-tan-xin-shou-ba-shou-jiao-xue-k-a0mp/
"""
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num = list(str(n))
        size = len(num)
        max_num = -1
        idx = -1
        for i in range(size - 1):
            if int(num[i]) > max_num:
                max_num = int(num[i])
                idx = i

            if num[i] > num[i+1]:
                num[idx] = str(int(num[idx]) - 1)
                for j in range(idx+1, size):
                    num[j] = '9'
                break
        return int(''.join(num))
