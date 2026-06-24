import pandas as pd

test=pd.read_csv('D:\Projects\Sample.csv')
#print(test)
test=test.rename(columns={"HomeTeam":"Homies"})

#time=test['Time']
#print(test)
max_value=test["FTHG"].max()
print(max_value)
count=(test['FTHG']==max_value).sum()
print(count)
sorted_test=test.sort_values(by='FTHG',ascending=False)
print(sorted_test)