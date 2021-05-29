#1st half of a is same as last half of b
a = [1,2,3,4]
x = len(a)//2
b = [5,6,1,2]
y = len(b)//2
if a[:x] == b[y:]:
    print('yes')
else:
    print('no')

a.sort(reverse=True)