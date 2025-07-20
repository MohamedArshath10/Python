def Monkeys():
    n = int(input("Enter the number of Monkeys : "))
    k = int(input("Enter the number of bananas monkey can eat : "))
    j = int(input("Enter the number of peanuts monkey can eat : "))
    m = int(input("Enter the number of total bananas : "))
    p = int(input("Enter the number of toal peanuts : "))
    newMonkey = 0
    for i in range(n):
        if(m >= k):
            m -= k
            newMonkey += 1
        elif(p >= j):
             p -= j
             newMonkey += 1
        elif m > 0 or p > 0:
            m=0
            p=0
            newMonkey += 1
    monkey = n - newMonkey
    print("The remaining Monkeys are : ",monkey)

Monkeys()