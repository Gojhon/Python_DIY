def cal(num1,num2,method='sum'):
    if method=='sum':
        print(num1+num2)
    elif method=='min':
        print(num1-num2)
    elif method=='prod':
        print(num1*num2)

print(cal(1,2))
print(cal(1,2,'prod'))
print(cal(1,2,'min'))
