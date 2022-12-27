# python program to extract unique values dictionary values

'''test_dict = {'A':[1,2,3,4], 'B': [3,5,7,9], 'C':[9,11,18,10], 'D':[10,12,11,15]}

print('The Original dictionary :' , test_dict)

result = list ( sorted ( { ele for val in test_dict.values() for ele in val } ) )

print('The Unique value list :', result)'''

numbers_list = [98,45,60,71,90]
count = 10
for number in numbers_list:
    if number % 10 == 0:
        count -= 1
        continue
    counter = 0
    while counter < 2:
        last_digit = number % 10
        number = number // 10
        if last_digit > 4:
            count += 1
            break
        count += 1
        counter += 1
print(count)