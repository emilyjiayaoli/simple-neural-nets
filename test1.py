def find():
    count = 1
    for i in range(8):
        temp = calculate(i)
        print(temp)
        if (temp * 10)%10 == 0 and (temp * 100)%100 == 0 and (temp * 1000)%1000 == 0:
            return i

find()
