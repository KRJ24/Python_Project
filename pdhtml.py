import pandas as pd

tables = pd.read_html("https://www.w3schools.com/html/html_tables.asp")

print(len(tables))
print(tables[0])
print(type(tables))

test=pd.read