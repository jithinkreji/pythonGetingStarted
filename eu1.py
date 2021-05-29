a = range(1000)
x = 0
for i in a:
    if i%3==0:
        x = x+i 
    elif i%5==0:
        x = x+i
print(x)