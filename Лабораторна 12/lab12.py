import json

def load_phonebook(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створюємо новий.")
        return {}
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")
        return {}

def save_phonebook(filename, phonebook):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(phonebook, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка запису у файл: {e}")

def find_phone_by_name(phonebook, name):
    phone = phonebook.get(name)
    if phone:
        print(f"Номер телефону {name}: {phone}")
    else:
        print(f"Інформація про {name} не знайдена.")

def find_name_by_phone(phonebook, number):
    for name, phone in phonebook.items():
        if phone == number:
            print(f"Номер {number} належить: {name}")
            return
    print(f"Номер {number} не знайдено в записнику.")

def print_all_entries(phonebook):
    if phonebook:
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Записник порожній.")

def add_entry(phonebook):
    name = input("Введіть прізвище: ")
    if name in phonebook:
        print("Цей запис вже існує.")
        return
    phone = input("Введіть номер телефону: ")
    phonebook[name] = phone
    print("Запис додано.")

def main():
    filename = "phonebook.json"
    phonebook = load_phonebook(filename)

    while True:
        print("\nМеню:")
        print("1 - Показати всі записи")
        print("2 - Додати новий запис")
        print("3 - Знайти телефон за прізвищем")
        print("4 - Знайти прізвище за номером")
        print("0 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print_all_entries(phonebook)
        elif choice == "2":
            add_entry(phonebook)
            save_phonebook(filename, phonebook)
        elif choice == "3":
            name = input("Введіть прізвище для пошуку: ")
            find_phone_by_name(phonebook, name)
        elif choice == "4":
            number = input("Введіть номер телефону для пошуку: ")
            find_name_by_phone(phonebook, number)
        elif choice == "0":
            print("Вихід із програми.")
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")

main()
