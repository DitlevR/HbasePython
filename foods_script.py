import happybase
import pandas as pd
import pdhbase as pdh

connection = happybase.Connection('localhost', port=16010, autoconnect=False)

connection.open()

table = connection.table("foods")

df = pd.read_excel("Food_Display_Table.xlsx")

##insert values
for index, row in df.iterrows():
    row_key = row[df.columns[0]]
    for col in df.columns[1:]:
        table.put(str(row_key), {"facts" + ':' + col: str(row[col])})

connection.close()
