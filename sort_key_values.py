# function definition
def sortkey():
    # declare hash function 
    key_value={}

    # initializing values
    key_value[2]=59
    key_value[1]=2
    key_value[5]=89
    key_value[4]=44
    key_value[6]=34
    key_value[3]=22

    print('Key value',key_value)
    # iterkeys() returns an iterator over the dictionary keys

    for i in sorted(key_value.keys()):
        print(i,end=' ')
    
sortkey()