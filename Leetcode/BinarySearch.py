num = [-1, 0, 3, 5, 9 ,12]
target = 10
found = False
for i in range(len(num)):
    if num[i] == target:
        print(i)
        found = True
        break
if not found:
    print(-1)