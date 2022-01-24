nums = [14,18,21,21]

for num in nums:

    if num % 5 ==0:
        print(num)
        break#break is compelsary here
else: #  in here the else is on the basis of for cuz when it comes under 'if' it will itrate and check the value and print it 5 times
        print('not found')