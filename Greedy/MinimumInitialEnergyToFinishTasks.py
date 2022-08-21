# -*- coding: utf-8 -*-
# @File    : MinimumInitialEnergyToFinishTasks.py
# @Date    : 2022-08-21
# @Author  : tc
"""
1665. 完成所有任务的最少初始能量
给你一个任务数组 tasks ，其中 tasks[i] = [actuali, minimumi] ：
actuali 是完成第 i 个任务 需要耗费 的实际能量。
minimumi 是开始第 i 个任务前需要达到的最低能量。
比方说，如果任务为 [10, 12] 且你当前的能量为 11 ，那么你不能开始这个任务。如果你当前的能量为 13 ，你可以完成这个任务，且完成它后剩余能量为 3 。
你可以按照 任意顺序 完成任务。
请你返回完成所有任务的 最少 初始能量。
示例 1：
输入：tasks = [[1,2],[2,4],[4,8]]
输出：8
解释：
一开始有 8 能量，我们按照如下顺序完成任务：
    - 完成第 3 个任务，剩余能量为 8 - 4 = 4 。
    - 完成第 2 个任务，剩余能量为 4 - 2 = 2 。
    - 完成第 1 个任务，剩余能量为 2 - 1 = 1 。
注意到尽管我们有能量剩余，但是如果一开始只有 7 能量是不能完成所有任务的，因为我们无法开始第 3 个任务。

示例 2：
输入：tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
输出：32
解释：
一开始有 32 能量，我们按照如下顺序完成任务：
    - 完成第 1 个任务，剩余能量为 32 - 1 = 31 。
    - 完成第 2 个任务，剩余能量为 31 - 2 = 29 。
    - 完成第 3 个任务，剩余能量为 29 - 10 = 19 。
    - 完成第 4 个任务，剩余能量为 19 - 10 = 9 。
    - 完成第 5 个任务，剩余能量为 9 - 8 = 1 。

示例 3：
输入：tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
输出：27
解释：
一开始有 27 能量，我们按照如下顺序完成任务：
    - 完成第 5 个任务，剩余能量为 27 - 5 = 22 。
    - 完成第 2 个任务，剩余能量为 22 - 2 = 20 。
    - 完成第 3 个任务，剩余能量为 20 - 3 = 17 。
    - 完成第 1 个任务，剩余能量为 17 - 1 = 16 。
    - 完成第 4 个任务，剩余能量为 16 - 4 = 12 。
    - 完成第 6 个任务，剩余能量为 12 - 6 = 6 。

为什么要根据 minimum - actual 排序？
因为 minimum表示的是"开始做这个任务的时候，拥有的最小能量值是多少"；
actual则是做这个任务所消耗的能量值。
所以，minimum - actual的结果，就是完成这个任务以后，剩余的能量值的最小值。
为了完成所有的任务，我们显然希望剩余的能量值越多越好。
所以，我们应该先完成“使得剩余的能量值多的任务”，即 minimum - actual 大的任务；
这样有更多的能量，去完成别的任务。
顺着这个思路，如果剩余的能量值一样的话，我们应该优先完成 minimum 较大的任务，也就是先把需要能量值比较多的任务完成。
（不然能量越来越少，后面就有可能完不成了。不过从数学的角度，这步似乎并不影响。）

思路：https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/solution/shi-yong-minimum-actual-pai-xu-de-zhi-jue-lai-zi-n/

"""
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # 按照剩余能量从大到小排序
        tasks.sort(key=lambda x:x[1] - x[0], reverse=True)
        # 完成所有任务需要的总能量
        ans = 0
        # 本次剩余的能量
        currEnergy = 0
        for cost, minimum in tasks:
            # 没有足够的能量开始本次任务
            if currEnergy < minimum:
                # 需要借额外的能量
                borrow = minimum - currEnergy
                ans += borrow
                # 本次剩余的能量
                currEnergy = minimum - cost
            else:
                # 不需要借额外的能量，但需要减去本次消耗的能量
                currEnergy -= cost
        return ans