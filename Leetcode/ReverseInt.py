x = 1534236469
b = 0
INT_MIN, INT_MAX = -2**31, 2**31 - 1
is_negative = x < 0
x = abs(x) #Covert -x into x

while x > 0:
    c = x % 10
    b = b * 10 + c
    x = x // 10

if is_negative:
    b = -b

if b < INT_MIN or b > INT_MAX:
    print(0)
else:
    print(b)


