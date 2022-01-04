n = int(input("Введите число элементов в массиве: "))

print("Введите", n , "элемента(ов) целочисленого массива через Enter: ")
arr = [int(input()) for i in range(n)]

# 1
for i in range(n):
# 2    
    min = i
# 3
    j = i + 1
# 4   
    for j in range(n):
# 5
        if (arr[j] < arr[min]):
# 6
            min = j
# 7           
        elif(min == i):
# 8
            t = arr[j]
            arr[j] = arr[min]
            arr[min] = t
# 9
        else:
            continue   

print("Результат: ", arr)

"""
1 - объявляем цикл по индексу i для arr[i], где - i от 0 до n
2 - обозначим элемент i как минимум  (в случае первой итерации - самый первый)
3 - последующий элемент за i обозначим как j
4 - организуем цикл, подобный для цикла i, только начинать будем с последующего j 
5 - проверяем условие: элемент массива j меньше минимального или нет
6 - если меньше - то он становится минимальным
7 - иначе выполняется условие - наш элемент i равен минимальному или нет 
8 - если условие выполняется - делаем перестановку элементов в массиве
минимального и j
9 - если не выполняется - идём на новый цикл по i, а затем j

"""
