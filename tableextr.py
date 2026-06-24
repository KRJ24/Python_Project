import pandas as pd

r= pd.read_csv('https://www.football-data.co.uk/mmz4281/2526/E0.csv')
r=r.rename(columns={'FTHG':'HomeGoals','FTAG':'AwayGoals'})
#print(r['Time'])
#print(r.columns)
max_val=r['HomeGoals'].max()
print(max_val)
count=(r['HomeGoals']==max_val).sum()
print(type(count))
print(type(r))