lst = list(map(int, input("Введіть список чисел: ").split()))

if len(lst) < 5:
    print("У списку менше п'яти елементів.")
else:
    top_five = sorted(lst, reverse=True)[:5]
    print("Перші п’ять максимальних елементів:", top_five)
