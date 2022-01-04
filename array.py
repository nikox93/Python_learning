n = int(input("Введите число элементов в массиве: "))

print("Введите", n , "элемента(ов) целочисленого массива через Enter: ")
arr = [int(input()) for i in range(n)] 

print("Результат: ", arr)
