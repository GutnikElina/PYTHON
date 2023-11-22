##Работа с Pandas и визуализация данных в Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Rooms': np.random.randint(1, 6, 1000),
    'District': np.random.choice(['Central', 'North', 'South', 'East', 'West'], 1000),
    'Price': np.random.randint(50000, 200000, 1000)
}

df = pd.DataFrame(data)
print(df)

df.to_csv('dataset.csv', index=False)

df = pd.read_csv('dataset.csv')
df_1000 = df.head(1000)
missing_data = df_1000.isnull().sum()

plt.figure(figsize=(10, 6))
plt.yscale('log')
df.boxplot()
plt.show()

df.hist()
plt.show()

mean_rooms = df['Rooms'].mean()
df['Rooms'] = df['Rooms'].fillna(mean_rooms)
df = df[(df['Price'] > 10000) & (df['Price'] < 200000)]

room_counts = df['Rooms'].value_counts()

pivot_df = df.pivot_table(index='District', columns='Rooms', values='Price', aggfunc='count')

pivot_df.index.name = 'Район'
pivot_df.columns = [f'{i}_комнатные' for i in pivot_df.columns]
print(pivot_df)

df.to_csv('surname.csv', index=False)
