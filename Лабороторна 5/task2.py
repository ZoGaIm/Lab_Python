n = 7

array = [[j - i + 1 if j >= i else 0 for j in range(n)] for i in range(n)]

for row in array:
    print(*row)
