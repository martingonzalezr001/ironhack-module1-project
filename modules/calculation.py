import geo_calculations
import pandas as pd
import argparse



def calculate_min_distance(df):
    df["distance(m)"] = df.loc[10000].apply(lambda row: geo_calculations.distance_meters(row["Latitude_bicimad"], row["Longitude_bicimad"], row["Latitude_place"], row["Longitude_place"]))
    min_distance = df["distance(m)"].min()
    df.to_csv(".\\data\\calculated_distances.csv",sep="\t")
    print(min_distance)
    
    return min_distance

def calculate_min_distance_specific(df):
    df = pd.read_csv(".\\data\\calculated_distances.csv")
    df["distance(m)"] = df.apply(lambda row: geo_calculations.distance_meters(row["Latitude_bicimad"], row["Longitude_bicimad"], row["Latitude_place"], row["Longitude_place"]))
    min_distance = df["distance(m)"].min()
    df.to_csv(".\\data\\calculated_distances.csv",sep="\t")
    print(min_distance)
    
    return min_distance

def define_final_df(df):
    distances_group = df.groupby(df["title"]).agg({"distance(m)":["idxmin","min"]}).reset_index()
    distances_group.columns = ["title", "idxmin","distancia_min(m)"] # To have our dataframe with a plain structure
    min_index = distances_group["idxmin"].dropna().astype(int) #Extracting the min index and drop NaN values 
    final_min_distances = df.loc[min_index] # Extracting rows with the index of the min values
    final_df = pd.merge(distances_group,final_min_distances[['title', 'address_bicimad_station', 'name_bicimad_station', 'address_name_place']], on="title", axis=1)
    
    return final_df

def rename_final_df(df):
    df["Type of place"] = "Espacio de deporte"
    df["Place of interest"] = df["title"]
    df = df.drop("title", axis=1)
    print(df)
    return df

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--f","--function", type=str, required=True, help="¿A qúe sitio te gustaría acudir en bicimad?")
    args = parser.parse_argparse()

