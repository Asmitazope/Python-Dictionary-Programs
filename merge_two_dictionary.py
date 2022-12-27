def merge(dict1,dict2):
    return(dict2.update(dict1))

dict1={'a':10,'b':20}
dict2={'c':30,'d':40}

print(merge(dict1,dict2))
print(dict2)