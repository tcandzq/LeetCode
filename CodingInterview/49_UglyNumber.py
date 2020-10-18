# -*- coding: utf-8 -*-
# @File    : 49_UglyNumber.py
# @Date    : 2020-10-18
# @Author  : tc
"""
剑指 Offer 49.丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/


下一个丑数一定是已有的某个丑数乘以2或者3或者5的结果，所以可以给每一个已有的丑数分别乘以2、3、5得到所有
可能的结果。现在的问题是，如何从所有的结果中知道最接近的丑数？因为题目要求丑数得按照从小到大的顺序排列。
我们可以设置三个指针, 分别指向第0行的1,2,3列(行列数从0开始算)":

要竖着看，才能看懂

    a b c
1 | 2 3 5 // 这一行里, 2,3,5分别是1乘以2,3,5的结果
2 | 4 6 10 // 同理, 4,6,10是2乘以2,3,5的结果
3 | 6 9 15 // ....
4 | 8 12 20

假设我们现在已经知道了已有的丑数序列为1,取第0行(2,3,5)的最小结果为2,此时取的是指针a指向的值;
因为我们要在一个比下一个未知的丑数都大的集合中寻找它，所以需要把指针a向下移动一行,让它指向4,其他指针不需要移动,因为理论上它们都可能比下一个丑数大,还需要在下一轮进行比较;
接着,求1,2的下一个丑数,只需要求(4,3,5)的最小值为3,此时让指针b往下移动一行,让它指向6
...

关键点：
1.保证a,b,c三个指针指向的数值一定要比当前的丑数要大;
2.可以发现,下一个丑数一定是a,b,c三者当中最小的那个;

思路参考：https://leetcode-cn.com/problems/chou-shu-lcof/solution/ni-jue-dui-neng-qing-song-kan-de-dong-de-chou-shu-/


代码参考：https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/

"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[i] == dp[a] * 2:
                a += 1
            if dp[i] == dp[b] * 3:
                b += 1
            if dp[i] == dp[c] * 5:
                c += 1
        return dp[n-1]



