##Работа с Pandas и визуализация данных в Matplotlib\

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Замените 'dataset.csv' на имя вашего файла датасета
df = pd.read_csv('dataset.csv')


subset_df = df.sample(n=1000, random_state=42)

missing_values = subset_df.isnull().sum()

# Построение ящиков с усами
sns.boxplot(x='column_name', y='target_column', data=subset_df)
plt.yscale('log')  # логарифмическая шкала
plt.show()

# Построение гистограммы
sns.histplot(subset_df['column_name'], kde=True)
plt.show()

##Заполнить пропуски и обработать аномальные значения.

room_counts = subset_df['колонка_с_количеством_комнат'].value_counts()

pivot_table = pd.pivot_table(subset_df, index='район', columns='колонка_с_количеством_комнат', aggfunc='size', fill_value=0)

subset_df.to_csv('surname.csv', index=False)
