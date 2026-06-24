import requests
import pandas as pd

df=pd.read_csv("D:\Project\Hashes.csv")

api_key="423feed2b74c6c5e14b1a147ac3f9e125ee3a573a217de12a51c3ea768de14dd"
headers = {"x-apikey": api_key}
vendors=['Microsoft','SentinelOne','CrowdStrike']

def hash_test(hash_list):
    
    for hashes in hash_list:
        url = f"https://www.virustotal.com/api/v3/files/{hashes}"
        response=requests.get(url,headers=headers)
        data=response.json()
        
        if response.status_code==200:
            print(f'Hash_value : {hashes}')
            stats=data['data']['attributes']['last_analysis_results']
            for vendor in vendors:
                if vendor in stats:
                    print (vendor,'=',stats[vendor]['category'] )                       
            print("\n")            
        else:
            print(f"Error occured for the hash_value : {hashes}, Error status_code :{response.status_code}")        

    
hash_test(df['hashes'])