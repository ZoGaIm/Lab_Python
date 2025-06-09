st = input("Введіть речення: ")
matching_words = []

for word in st.split():
    clean_word = word.strip(".,!?;:-()\"'")

    if len(clean_word) >= 2 and clean_word[0].lower() == clean_word[-1].lower():
        matching_words.append(clean_word)

if matching_words:
    print("Слова, які починаються і закінчуються на ту саму літеру:")
    print(", ".join(matching_words))
else:
    print("Немає таких слів.")
