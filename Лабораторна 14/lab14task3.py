import json
import matplotlib.pyplot as plt
from collections import Counter

with open("phonebook.json", "r", encoding="utf-8") as jsonfile:
    data = json.load(jsonfile)

counts = Counter(data.keys())

names = list(counts.keys())
counts_values = list(counts.values())

fig, ax = plt.subplots()
ax.pie(counts_values, labels=names, autopct='%1.1f%%')
plt.title("Розподіл телефонних номерів за прізвищами")
plt.axis('equal')
plt.legend()
plt.show()
