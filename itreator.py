nums =[53,34,35,53,6,44,5]
# for i in nums:
#     print(i)


it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.num<10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

values = Topten()

print(next(values))
for i in values:
    print(i)

