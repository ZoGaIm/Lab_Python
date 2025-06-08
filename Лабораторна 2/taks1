import math

def calculate_z(a):
    z = (math.sqrt(2) / 2) * math.sin(a / 2)
    return z

def count_amoebas(n):
    divisions = n // 3
    count = 2 ** divisions 
    return count

def main():
    a = float(input("Введіть значення a (в радіанах): "))
    z = calculate_z(a)
    print(f"Значення z: {z:.4f}")

    n = int(input("Введіть кількість годин (n): "))
    amoebas = count_amoebas(n)
    print(f"Кількість амеб через {n} годин: {amoebas}")

main()
