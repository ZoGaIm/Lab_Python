a = int(input("������ a:"))
while (a <= 0):
    print("a ������ ����� ������ ��������!")
    a = int(input("������ a:"))
b = int(input("������ b:"))
while (b <= 0):
    print("b ������ ����� ������ ��������!")
    b = int(input("������ b:"))
x = 0
if a > b:
    x = a/b - 1
elif a == b:
    x = -25
else :
    x = (a**3-5)/a
print(f"X = {x}")

