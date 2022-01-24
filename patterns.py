# for i in range(4):
#     if i <=4:
#         print('# # # #')
#
#     i = i+1
          #or
# for i in range(4):
#     for j in range(4):
#         print('#',end=" ")
#
#     print()

# for i in range(5,1,-1):
#     for j in range(i-1):
#         print("#",end=' ')
#     print()
         #0r
for i in range(4):
    for j in range(4-i):
        print("#", end= " ")

    print()