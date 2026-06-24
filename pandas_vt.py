import requests
import time
import pandas as pd
df=pd.read_csv(r"C:\Users\2410k\Downloads\hashes.csv")
headers={'x-apikey':''}

def hash_fn(hash_val):
    url=f'https://www.virustotal.com/api/v3/files/{hash_val.strip()}'
    response=requests.get(url,headers=headers)
    
    try:
        data=response.json()
        stats=data['data']['attributes']['last_analysis_stats']
        stats1=data['data']['attributes']['names']
        code_stat=(response.status_code)
        if code_stat == 200:
            for items in stats1:
                print(f'Name of the file = {items}')
                break
            print("Find The detection details below:")
            for key, values in stats.items():
                print(f"Malicious count = {stats['malicious']}\nSuspicious count = {stats['suspicious']}\nUndetected count = {stats['undetected']}\n")
                break    
    except Exception as e:
        print(f'Unexpected error for {hash_val}, error returned = {e}\n') 
    time.sleep(5)
    #print(type(stats))
def csv_file(d_frame):

    for index,row in df.iterrows():
        a=row['Hashes']
        hash_fn(a)
        

csv_file(df)

