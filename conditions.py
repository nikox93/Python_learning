speed = int(input("Введите скорость автомобиля: "))


if(speed == 0):
    print("Автомобиль стоит на месте")
elif(speed < 0 or speed > 200):
    print("Нет такой скорости")
elif(speed > 60):
    print("Нарушение")
else:
    print("В пределах нормы")
