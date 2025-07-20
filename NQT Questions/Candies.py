def Candies(n):
    total = 10
    if n > total:
        print("INVALID INPUT")
        return
    else:
        if n == 0:
            print("INVALID INPUT")
            print("the number of candies in the jar: ", total - n)
        elif total >=5:
            print("the number of candies sold: ",n)
            print("the number of candies in the jar: ", total - n)
            total = 10
            print("refilled the jar in the jar: ", total)


n = int(input("Enter a number: "))
Candies(n)