#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-12-17 下午5:58
# @Author  : KainHuck
# @Email   : kainhoo2333@gmail.com
# @File    : 无向图邻接表.py

import copy

class ArcNode():
    '''定义边类'''
    def __init__(self, node_container):
        self.node_container = node_container                          # 存放头尾结点的列表
        self.node_info_list = []
        for each in node_container:
            self.node_info_list.append(each.info)

class VNode():
    '''定义结点类'''
    def __init__(self, info):
        self.info = info                                              # 结点的名字
        self.next_one = None                                          # 用于链接下一个结点

def built_table(Node_list, Arc_list):
    '''构造邻接表,参数为结点列表和边列表'''
    for each_node in Node_list:                                       # 循环每个节点
        temp_list = []                                                # 存放和当前结点相邻的结点
        for each_arc in Arc_list:                                     # 通过边来判断哪些结点相邻
            if each_node.info in each_arc.node_info_list:             # 找到相邻的结点
                all_index = [0, 1]                                    # 储存边的列表的所有位置
                now_index = each_arc.node_info_list.index(each_node.info)  # 当前结点在边的列表里的位置
                all_index.remove(now_index)                           # 删除当前的位置
                true_index = all_index.pop()                          # 获取剩下的结点的位置
                temp = copy.copy(each_arc.node_container[true_index]) # 相邻结点的浅拷贝
                temp_list.append(temp)                                # 加入列表

        try:                                                          # 没有相邻结点的情况
            each_node.next_one = temp_list[0]                         # 当前结点指向找到的第一个结点
            for i in range(len(temp_list) - 1):                       # 循环连接
                temp_list[i].next_one = temp_list[i+1]
            temp_list[len(temp_list)].next_one = None                 # 最后一个为None
        except:
            pass

    # 打印邻接表
    flag = 0
    for each_node in Node_list:
        print(flag, ' ', end='')
        while each_node.next_one != None:
            print(each_node.info, '-> ', end='')
            each_node = each_node.next_one
        print(each_node.info, '-> None')
        flag += 1

if __name__ == '__main__':
    Node_num = int(input("请输入无向图结点的个数:"))
    Node_list = []                                                     # 储存结点的列表

    # 初始化所有的结点
    for i in range(Node_num):
        info = input("请输入第%d个结点的名字:" % (i+1))
        temp_node = VNode(info)                                        # 构造结点
        Node_list.append(temp_node)                                    # 加入列表

    Arc_num = int(input("请输入无向图的边数:"))
    Arc_list = []                                                      # 储存边的列表

    # 初始化所有的边
    for i in range(Arc_num):
        head_node_num = int(input("请输入第%d条边所连的第一个结点序号:" % (i+1)))
        next_node_num = int(input("请输入第%d条边所连的下一个结点的序号:" % (i+1)))
        head_node = copy.copy(Node_list[head_node_num - 1])
        next_node = copy.copy(Node_list[next_node_num - 1])
        node_container = [head_node, next_node]
        temp_arc = ArcNode(node_container)                             # 构造边
        Arc_list.append(temp_arc)                                      # 加入列表

    # 构造邻接表
    built_table(Node_list, Arc_list)





















