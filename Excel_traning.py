# Импортируем библиотеку pandas и datetime - для работы с датами
import pandas as pd
from pandas import Series, DataFrame
import datetime
from datetime import datetime, date
#Задаем некоторые опции библиотеки PandasЮ которые настраивают вывод
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.width', 100)

#Загружаем файл в переменную
file = '149_0503124-3_TOFK_2020_04_07_05_57_17.xlsx'
xl = pd.read_excel(file, u'Тест')
#print(xl)

# Задаем индексы, стобцы и значения
index = xl.index
columns = xl.columns
values = xl.values

# Создаем списки индексов, стобцов и значений
index_list = xl.index.tolist()
columns_list = xl.columns.tolist()
values_list = xl.values.tolist()

# Выводим значения определенных столбцов (если один столбец одинарные - [] - Series, если перечисление то двойные [] - DataFrame)
print(xl[['ЦСР', '0503124 Утвержденные бюджетные назначения']])








