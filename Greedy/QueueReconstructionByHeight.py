"""
题号 406 根据身高重建队列
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

看了评论才读懂题意

思路参考:https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/406-gen-ju-shen-gao-zhong-jian-dui-lie-java-xian-p/

代码参考:https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/python-5-xing-ti-jie-by-hellozhaozheng/

"""
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])  # 先根据x[0]降序，再根据x[1]升序。此时有[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    solution = Solution()
    print(solution.reconstructQueue(people))