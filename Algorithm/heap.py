#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 17:39
# @Author  : tc
# @File    : heap.py
"""
满二叉树:除了最下面一层之外,其余各层的结点个数都达到了当前层能达到的最大点数,并且最下面一层从左至右连续存在若干结点,而这
些连续结点全部不存在。
说人话:完全二叉树从根结点到倒数第二层满足完美二叉树，最后一层可以不完全填充，其叶子结点都靠左对齐。
"""

"""
向下调整的过程如下:
总是将当前结点V与它的左右孩子比较(如果有的话),假设孩子中存在权值比结点V的权值大的,就将其中权值最大的那个孩子结点与结点V交换;
交换完毕后继续让结点V和孩子比较,直到结点V的孩子结点的权值都比结点V的权值小或者不存在孩子结点。

"""
def down_adjust(low,high,heap):
    i = low
    j = i * 2  #i为欲调整结点,j为其左孩子
    while j <= high: #存在孩子结点
        #如果右孩子存在,且右孩子的值大于左孩子
        if j+1 <= high and heap[j+1] > heap[j]:
            j += 1    #让j存储右孩子的位置

        #如果孩子中最大的权值比欲调整的结点i大
        if heap[j] > heap[i]:
            heap[j], heap[i] = heap[i], heap[j] #交换最大权值的孩子与欲调整结点i
            i = j   #保持i为欲调整结点,j为i的左孩子
            j = i*2
        else:
            break

#建堆的过程
"""
假设序列中的元素个数为n,由于完全二叉树的叶子结点个数为[n/2]
"""
def create_heap(n,heap):
    for i in range(n//2, 0, -1):
        down_adjust(i,n,heap)

#删除推顶元素
def delete_top(heap,n):
    heap[1] =heap[n]  # 用最后一个元素覆盖堆顶元素
    n -= 1           # 让元素个数减1
    down_adjust(1,n,heap) #向下调整堆顶元素


# 向上调整操作
# 对heap数组在[low,high]范围内进行向上调整
# 其中low一般设置为1,high表示欲调整结点的数组下标
def up_adjust(low,high,heap):
    i = high   # i为欲调整的结点
    j = i // 2  # j为其父结点
    while j >= low:  # j在[low,high]的范围内
        if heap[j] < heap[i]:  # 父亲结点的权值小于欲调整结点的权值
            heap[j],heap[i] = heap[i],heap[j]  #交换父结点和欲调整结点
            i = j  # 保持i为欲调整结点,j为i的父结点
            j = i // 2
        else:
            break


#添加元素x
def insert(x,heap,n):
    n += 1    # 让元素个数加1
    heap[n] = x  # 将数组末位赋值为x
    up_adjust(1,n,heap) # 向上调整新加入的结点n


#堆排序
def heap_sort(n,heap):
    create_heap(n,heap)   # 建堆
    for i in range(n,2,-1):  # 倒着枚举,直到堆中只有一个元素
        heap[i],heap[1] = heap[1],heap[i]  # 交换heap[i]与堆顶
        down_adjust(1,i-1,heap)  # 调整堆顶

