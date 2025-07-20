arr1 = []
arr2 = []
sum1 = 0
sum2 = 0
num1 = int(input("Enter a number for exterior: "))
for num in range(num1):
    arr1.append(float(input("Enter a number: ")))
    sum1 += arr1[num]
num2 = int(input("Enter another number for interior: "))
for num in range(num2):
    arr2.append(float(input("Enter another number: ")))
    sum2 +=arr2[num]
print("The exterior painting cost is : ",sum1*18)
print("The interior painting cost is : ",sum2*12)
print("Total sum: ", sum1*18 + sum2*12)