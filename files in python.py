#to open an existing file
# o = open('content','r')
# print(o.read())
# f=open('c1','w')
# print(f.write('something'))
f=open('c1','r')
print(f.read())
# f1=open('c1','a')
# print(f1.write('hellow'))
f1 = open('content.txt','w')

# for data in f:
#     print(data)
for data in f:
    f1.write(data) #to combine two files with data