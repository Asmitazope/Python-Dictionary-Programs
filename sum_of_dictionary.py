# python program to find the sum of all items in dictionary

def dictSum(mydict):
    sum_item = 0
    for i in mydict.values():
        sum_item = sum_item + i
    return sum_item

my_dict = { 'a':100, 'b': 200, 'c': 300, 'd': 400}
print('sum:', dictSum(my_dict))