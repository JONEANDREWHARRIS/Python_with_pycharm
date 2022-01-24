pos =-1
def search(list,n):
    i =0
    while i<len(list):
        if list[i] ==n:
            globals()['pos'] =i
            return True
        i = i+1
    return False

list = [5,3,2,5,1,7,4,3,50]
n =4
if search(list, n):
    print('found at',pos)
else:
    print('not found')