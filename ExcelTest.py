import pandas as pd
from pandas import ExcelWriter

data1 = pd.DataFrame({"a": [1,2,3], "b": [3,4,5]})
data2 = pd.DataFrame({"x": [33,22,11,00.001], "y": [11, 22, 33, 44], "z": [423, 234, 234, 2222]})


print(data1)
print(data2)

writer = ExcelWriter("gg.xlsx")

data1.to_excel(writer, "tab1")
data2.to_excel(writer, "tab_gg")

writer.save()