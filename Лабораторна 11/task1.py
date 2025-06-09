import csv

try:
    with open("gdp_per_capita.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        usa_data = None

        for row in reader:
            if row["Country Name"] == "United States":
                usa_data = row
                break

        if not usa_data:
            print("Дані для США не знайдено!")
        else:
            print("GDP per capita (current US$) для США (1991–2019):")
            gdp_data = {}
            for year in range(1991, 2020):
                year_str = str(year)
                value = usa_data.get(year_str, "")
                if value:
                    gdp_data[year] = float(value)
                    print(f"{year}: {value}")
                else:
                    print(f"{year}: дані відсутні")

            min_year = min(gdp_data, key=gdp_data.get)
            max_year = max(gdp_data, key=gdp_data.get)

            print("\nНайнижче значення:")
            print(f"{min_year}: {gdp_data[min_year]}")

            print("\nНайвище значення:")
            print(f"{max_year}: {gdp_data[max_year]}")

            with open("usa_gdp_stats.csv", "w", newline='',
                      encoding="utf-8") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(["Тип", "Рік", "Значення"])
                writer.writerow(["Мінімум", min_year, gdp_data[min_year]])
                writer.writerow(["Максимум", max_year, gdp_data[max_year]])

            print("\nРезультати записано у файл usa_gdp_stats.csv")

except FileNotFoundError:
    print("Файл gdp_per_capita.csv не знайдено!")

except Exception as e:
    print(f"Помилка виконання програми: {e}")
