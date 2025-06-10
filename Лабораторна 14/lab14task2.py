import matplotlib.pyplot as plt
import numpy as np
import csv

years = []
ukraine = []
poland = []

try:
    with open("gdp-per-capita-poland-ukraine.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row['Country Name'] == "Ukraine":
                for year in range(2003, 2024):
                    years.append(year)
                    ukraine.append(float(row[f"{year} [YR{year}]"]))
            elif row['Country Name'] == "Poland":
                for year in range(2003, 2024):
                    poland.append(float(row[f"{year} [YR{year}]"]))

except FileNotFoundError:
    print("Фай gdp-per-capita-poland-ukraine.csv не знайдено!")
    exit(0)

years = np.array(years)
ukraine = np.array(ukraine)
poland = np.array(poland)

plt.plot(years, ukraine, label='Ukraine', color="blue")
plt.plot(years, poland, label='Poland', color="red")

plt.title('GDP per capita', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('US$', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()

