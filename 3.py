a = input('enetr a')
a = int(a)
b = input('enetr b')
b = int(b)
choice = input('enetr your command')
if choice == '1':
    print('{ar} + {rr} = {gg} '.format(ar=a, rr=b, gg=a+b))
    # print(a, '+', b, '=', a+b)
elif choice == '2':
    print(a, '-', b, '=', a-b)
elif choice == '3':
    print(a, '/', b, '=', a/b)
elif choice == '4':
    print('rm of ', a, '/', b, '=', a % b)
elif choice == '5':
    print('product of', a, 'and', b, '=', a*b)
else:
    print('invalid choice')

