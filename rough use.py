# import os


# l =[32,424,2,3,4,22,34,2,23]
# def searchminfromlist(l,n):
#     min_value = l[0]
#     counter = 1
#     while counter <=n:
#         v =l[counter]
#         if v<min_value:
#             min_value = v
#             idx = counter
#         else:
#             pass
#         return min_value,idx
# def sort(l,n):
#     l2 =[]
#     counter = 0
#     while counter<=n:
#         m,idx=searchminfromlist(l,n)
#         l2.append(m)
#         del l[idx]
#         n = n-1
#     return l2
# x =4
# y =5
# z =2
# pow(x,y,z)

# tuple ={}
# tuple[(1,2,4)] =8
# tuple[(4,2,1)] = 10
# tuple[(1,2)] =12
# sum_in =0
# for k in tuple:
#     sum_in+=tuple[k]
# # print(len(tuple)+sum_in)
# line = '*'
# max_length = 10
#
# while len(line) <= max_length:
#     print(line)
#     line += "*"
#
# while len(line) > 0:
#     print(line)
#     line = line[:-1]
# list = [1, 1, 2, 3, 5, 8, 13]
# # print(list[list[4]])
# # def func(x):
# #   res = 0
# #   for i in range(x):
# #      res += i
# #   return res
# #
# # print(func(4))
# # letters = ['x', 'y', 'z']
# # letters.insert(1, 'w')
# # print(letters[2])
# a=5
# b=10
# print(a|b)
# print(b<<a)
# Python3 program to demonstrate linked list
# based implementation of queue

# A linked list (LL) node
# to store a queue entry
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# # A class to represent a queue
#
# # The queue, front stores the front node
# # of LL and rear stores the last node of LL
# class Queue:
#
#     def __init__(self):
#         self.front = self.rear = None
#
#     def isEmpty(self):
#         return self.front == None
#
#     # Method to add an item to the queue
#     def EnQueue(self, item):
#         temp = Node(item)
#
#         if self.rear == None:
#             self.front = self.rear = temp
#             return
#         self.rear.next = temp
#         self.rear = temp
#
#     # Method to remove an item from queue
#     def DeQueue(self):
#
#         if self.isEmpty():
#             return
#         temp = self.front
#         self.front = temp.next
#
#         if (self.front == None):
#             self.rear = None
#
#
# # Driver Code
# if __name__ == '__main__':
#     q = Queue()
#     q.EnQueue(1)
#     q.EnQueue(20)
#     q.DeQueue()
#     q.DeQueue()
#     q.EnQueue(3 )
#     q.EnQueue(40)
#     # q.EnQueue(50)
#     # q.DeQueue()
#     print("Queue Front " + str(q.front.data))
#     print("Queue Rear " + str(q.rear.data))
def first_num(numlist):
    return numlist
