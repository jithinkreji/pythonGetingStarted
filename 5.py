a = [1,2,3,4]
b = list(range(4,0,-1))
if a == b[::-1]: 
    print('yes')
else:
    print('no')