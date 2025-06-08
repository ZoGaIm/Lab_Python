a = int(input("¬вед≥ть a:"))
while (a <= 0):
    print("a приймаЇ т≥льки додатн≥ значенн€!")
    a = int(input("¬вед≥ть a:"))
b = int(input("¬вед≥ть b:"))
while (b <= 0):
    print("b приймаЇ т≥льки додатн≥ значенн€!")
    b = int(input("¬вед≥ть b:"))
x = 0
if a > b:
    x = a/b - 1
elif a == b:
    x = -25
else :
    x = (a**3-5)/a
print(f"X = {x}")

