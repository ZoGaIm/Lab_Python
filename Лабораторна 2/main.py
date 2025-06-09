from mod import count_amoebas

def main():
    try:
        n = int(input("Введіть кількість годин (n): "))
        if n < 0:
            print("Кількість годин не може бути від'ємною.")
            return

        result = count_amoebas(n)
        print(f"Кількість амеб через {n} годин: {result}")

    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
