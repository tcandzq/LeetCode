"""
题号 155 最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

参考:https://leetcode-cn.com/problems/min-stack/solution/shi-yong-fu-zhu-zhan-tong-bu-he-bu-tong-bu-python-/

"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        if len(self.helper) == 0 or x <= self.helper[-1]:  # 注意这里是等号
            self.helper.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        top = self.stack.pop(-1)
        if self.helper and top == self.helper[-1]:
            self.helper.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
