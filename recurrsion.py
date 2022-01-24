import sys
sys.setrecursionlimit(45)

print(sys.getrecursionlimit())
u= 0
def greet():
    global u
    u+=1
    print('hello')
    greet()
greet()
# if we use greet() here it will print hello for the above value which is 455555times



