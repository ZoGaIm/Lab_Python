word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

unique_letters = []

for letter in word1:
    if letter not in word2:
        unique_letters.append(letter)

for letter in word2:
    if letter not in word1:
        unique_letters.append(letter)

if unique_letters:
    print("Літери, які є тільки в одному зі слів (включаючи повторення):")
    print("".join(unique_letters))
else:
    print("Усі літери зустрічаються в обох словах.")
