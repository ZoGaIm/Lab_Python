import pandas as pd
import matplotlib.pyplot as plt

fixed_df = pd.read_csv('comptagevelo2010.csv',
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')

fixed_df = fixed_df.dropna(axis=1, how='all')
fixed_df = fixed_df.apply(pd.to_numeric, errors='coerce').fillna(0)
daily_df = fixed_df.resample('D').sum()
most_popular_month = daily_df.sum(axis=1).idxmax()

print(f"Найпопулярніший місяць: {most_popular_month.strftime('%B %Y')}")
print(f"Кількість відвідувань: {daily_df.sum(axis=1).max()}")

plt.figure(figsize=(15, 8))
daily_df.plot(kind='line', title='Monthly Cycling Path Visits', grid=True)
plt.ylabel('Number of Visits')
plt.xlabel('Month')
plt.show()
