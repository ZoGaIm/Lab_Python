N = int(input("������ N: "))
while N <= 1 or N >= 9:
    print("N ������� ������������ 1<N<9!")
    N = int(input("������ N: "))

for i in range(1, N + 1):  
    currentRow = ""
    for j in range(N, N - i, -1):  
        currentRow += str(j) + " "
    print(currentRow)

