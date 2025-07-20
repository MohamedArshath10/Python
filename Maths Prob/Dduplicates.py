def Duplicate1(n):
    unique = []
    for i in range(len(my_list)):
        for j in range(i):
            if my_list[i] == my_list[j]:
                break
        else:
            unique.append(my_list[i])
    print(unique)

# The fastest method
def Duplicate2(n):
    unique = list(dict.fromkeys(n))
    print(unique)

my_list = [7,10,1,2,3,4,1,2,7,1,8,9]
Duplicate1(my_list)
Duplicate2(my_list)
