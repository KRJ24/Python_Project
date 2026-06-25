import requests
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
        #print(code_stat)
        if code_stat == 200:
            for items in stats1:
                file_name=items
                break
            #print("Find The detection details below:")
            for key, values in stats.items():
                #print(f"Malicious count = {stats['malicious']}\nSuspicious count = {stats['suspicious']}\nUndetected count = {stats['undetected']}\n")
                mal_count=stats['malicious']
                sus_count=stats['suspicious']
                undetect_count=stats['undetected']
                break    
        return {'Hash_value':hash_val.strip(),'name':file_name,'malcount': mal_count,'suspicious': sus_count,'undetected':undetect_count}    
    except:
        except_raw= { 'Hash_value': hash_val.strip(),'name': 'ERROR','malcount': 'ERROR','suspicious': 'ERROR','undetected': 'ERROR'}
        return except_raw
    #print(type(stats))

def read_df(df):
    output_list=[]
    for index,row in df.iterrows():
        a = hash_fn(row['Hashes'])    
        output_list.append(a)  
    return output_list

out_dict=read_df(df)
hash_list=[]
name_list=[]
mal_list=[]
sus_list=[]
und_list=[]
for items in out_dict:
    for key, value in items.items():
        #print(key)
        if key=='Hash_value':
            hash_list.append(items[key])
        if key=='name':
            name_list.append(items[key])
        elif key=='malcount':
            mal_list.append(items[key])    
        elif key=='suspicious':
            sus_list.append(items[key])
        elif key=='undetected':
            und_list.append(items[key])

#print(hash_list,name_list,mal_list,sus_list,und_list)
final_out=pd.DataFrame({'Hash_value':hash_list,"Filename":name_list,'Malicious count':mal_list,'Suspicious Count':sus_list,'Undetected count':und_list})
final_out.to_csv(r"C:\Users\2410k\Downloads\Hash_Validation_final_output.csv",index=False)
print(r"Kindly find the hash Validation output file in the location => C:\Users\2410k\Downloads\Hash_Validation_final_output.csv ")

   