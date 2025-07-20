def Oxygen():
    traineeSum1 = 0
    traineeSum2 = 0
    traineeSum3 = 0
    for _ in range(3):
        attempt1 = int(input("Enter a number: "))
        traineeSum1 += attempt1
        attempt2 = int(input("Enter a number: "))
        traineeSum2 += attempt2
        attempt3 = int(input("Enter a number: "))
        traineeSum3 += attempt3


    avgTrainee1 = traineeSum1 // 3
    avgTrainee2 = traineeSum2 // 3
    avgTrainee3 = traineeSum3 // 3
    print(avgTrainee1, avgTrainee2, avgTrainee3)
    maxAvg = max(avgTrainee1, avgTrainee2, avgTrainee3)
    trainee = []
    if maxAvg == avgTrainee1:
        trainee.append(1)
    if maxAvg == avgTrainee2:
        trainee.append(2)
    if maxAvg == avgTrainee3:
        trainee.append(3)

    for i in trainee:
        print("trainee" , str(i))

Oxygen()