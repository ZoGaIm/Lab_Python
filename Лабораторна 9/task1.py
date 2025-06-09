def create_file_tf8_1():
    content = (
        "Це 1тестовий рядок з лі123терами і цифрами. "
        "Ще один ря2док, в якому є цифр4и, і си66мволів. "
        "Програма пови4нна видалити всі цифри і роз33бити текст."
    )

    try:
        with open("TF8_1.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print("Файл TF8_1.txt створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")


def transform_file_tf8_1_to_tf8_2():
    try:
        with open("TF8_1.txt", "r", encoding="utf-8") as file:
            content = file.read()

        cleaned_text = ''.join([c for c in content if not c.isdigit()])

        with open("TF8_2.txt", "w", encoding="utf-8") as file:
            for i in range(0, len(cleaned_text), 10):
                line_number = i // 10 + 1
                line = cleaned_text[i:i + 10]
                file.write(f"{line_number:05} {line}\n")

        print("Файл TF8_2.txt створено з форматованим текстом.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")


def print_file_tf8_2():
    print("\nВміст файлу TF8_2.txt:")
    try:
        with open("TF8_2.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Помилка при читанні файлу TF8_2.txt: {e}")


def main():
    create_file_tf8_1()
    transform_file_tf8_1_to_tf8_2()
    print_file_tf8_2()


main()
