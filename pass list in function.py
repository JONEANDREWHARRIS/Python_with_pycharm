
def count(lst):
    even =0
    odd = 0

    for i in lst:
        if i%2 ==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst = [24 ,84, 42,7, 424, 24]

even, odd = count(lst)
print(even)
print(odd)
## my assignment
def person(lst):
    short_name =0
    too_big = 0

    for i in lst:
        if len(i) ==5:
            short_name+=1
        else:
            too_big+=1

    return short_name,too_big

lst = ['jone','andrew','harris','shiny']

short_name, too_big = person(lst)
print(short_name)
print(too_big)