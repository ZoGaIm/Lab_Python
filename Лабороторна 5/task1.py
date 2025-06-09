N = int(input("Введіть довжину масиву N: "))
print("Введіть елементи масиву:")

array = [int(input(f"Елемент {i + 1}: ")) for i in range(N)]

if array:
    min_element = min(array)
    print("Мінімальний елемент масиву:", min_element)
else:
    print("Масив порожній.")
