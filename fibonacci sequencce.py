def fib(n):

    a = 0
    b = 1
    if n <=0:
        print('invalid')
    elif n ==1:
        print(a)

    else:
        print(a)
        print(b)

    for i in range(2,n):
        c = a+b
        a =b
        b =c
        if c >100: #0r use n
            break
        else:

           print(c)

fib(300)