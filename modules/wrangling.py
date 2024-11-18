#  To clean and transform the data
import pandas as pd


def clean_data(df):
    
    df["geometry.coordinates_tmp"] = df["geometry.coordinates"]
    df["geometry.coordinates_tmp"] = df["geometry.coordinates_tmp"].str.strip("[]")
    df["geometry.coordinates_tmp"] = df["geometry.coordinates_tmp"].str.replace(",","")
    df["geometry.coordinates_tmp"] = df["geometry.coordinates_tmp"].str.split(" ")

    df["Longitud"] = df["geometry.coordinates_tmp"].apply(transform_longitud)
    df["Latitud"] = df["geometry.coordinates_tmp"].apply(transform_latitud)
    #print(df)
    return df

def clean_dict_data(df):
    df["latitud"] = df["location"].apply(transform_latitude_dict)
    df["longitud"] = df["location"].apply(transform_longitude_dict)
    #print(df)
    return df

def get_address_name(df):
    df_dir = df.loc[:,"address"]
    #for key, values in df_dir.items(): # We check that the street address is in direction
    #    print(str(key) + " : " + str(values))
    serie_places_address = df_dir.apply(lambda x: x.get('street-address'))# We extract the street address
    df["address_name"] = serie_places_address
    #print(df)
    return df

def rename_bicimad_columns(df):
        # Before the merge Im going to change the names of latitude and longitude to be able to different them when they will be merged
    df["Latitude_bicimad"] = df["Latitud"]
    df["Longitude_bicimad"] = df["Longitud"]

    # The same with the address columns to not to provoque understanding problems
    df["address_bicimad_station"] = df["address"]
    df["name_bicimad_station"] = df["name"]
    # Dropping columns with the previous name
    
    df = df.drop('Latitud',axis=1)
    df = df.drop('Longitud',axis=1)
    df = df.drop('address',axis=1)
    df = df.drop('name', axis=1)
    return df

def rename_places_columns(df):
    df["Latitude_place"] = df["latitud"]
    df["Longitude_place"] = df["longitud"]  
    df["address_name_place"] = df["address_name"] 

    df = df.drop('latitud',axis=1)
    df = df.drop('longitud',axis=1)
    df = df.drop('address_name', axis=1)
    #print(df)

    return df


def merge_dataframes(df,df2):
    df_to_merge = df[['address_bicimad_station','name_bicimad_station','Latitude_bicimad','Longitude_bicimad']].copy()
    df2_to_merge = df2[['title','address_name_place','Latitude_place','Longitude_place']].copy()

    df_to_merge["key"] = 1
    df2_to_merge["key"] = 1

    df_merged = pd.merge(df_to_merge, df2_to_merge, on='key',how='inner')
    df_merged = df_merged.drop('key', axis=1) # Now we dont need it
    

    #print(df_merged)
    return df_merged



def transform_longitud(location): 
    return location[0]
def transform_latitud(location): 
    return location[1]

def transform_latitude_dict(location):
    latitude = location["latitude"]
    return latitude

def transform_longitude_dict(location):  
    longitude = location["longitude"]
    return longitude
