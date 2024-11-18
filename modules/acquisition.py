#To import our data and create our DataFrames

import pandas as pd
import requests


def read_save_csv(url1):
    df1 = pd.read_csv(url1,sep='\t')
    print(df1)
    return df1

def read_save_json(url2):
    response = requests.get(url2)
    sitios_data = response.json()

    for keys, values in sitios_data.items():
        if keys == "@graph":
            data_list = values

    df_sitios = pd.DataFrame(data_list)

    print(df_sitios)

    return df_sitios

