#Imports:
import json
from shapely.geometry import Point
import geopandas as gpd
import acquisition
import wrangling
import calculation
import timeit
import argparse



def argument_parser():
    parser = argparse.ArgumentParser(description= 'Application for bicimad finder' )
    help_message ='Introduce \'todos\' o un centro deportivo desde el que quieras ir' 
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    if argument_parser().function == 'todos':
        
        url_data_bicimad = ".\\data\\bicimad_stations.csv"
        url_data_sitios = "https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json"


        df_bicimad = acquisition.read_save_csv(url_data_bicimad)
        df_sitios = acquisition.read_save_json(url_data_sitios)

        df_bicimad = wrangling.clean_data(df_bicimad)
        df_sitios = wrangling.clean_dict_data(df_sitios)

        df_sitios = wrangling.get_address_name(df_sitios)

        df_bicimad = wrangling.rename_bicimad_columns(df_bicimad)
        df_sitios = wrangling.rename_places_columns(df_sitios)

        df_merged = wrangling.merge_dataframes(df_bicimad,df_sitios)
        min_distance = calculation.calculate_min_distance(df_merged)
        final_df = calculation.define_final_df(df_merged)
        final_df = calculation.rename_final_df(final_df)
        print(final_df)


    elif argument_parser().function == 'sitio':
        url_data_bicimad = ".\\data\\bicimad_stations.csv"
        url_data_sitios = "https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json"


        df_bicimad = acquisition.read_save_csv(url_data_bicimad)
        df_sitios = acquisition.read_save_json(url_data_sitios)

        df_bicimad = wrangling.clean_data(df_bicimad)
        df_sitios = wrangling.clean_dict_data(df_sitios)

        df_sitios = wrangling.get_address_name(df_sitios)

        df_bicimad = wrangling.rename_bicimad_columns(df_bicimad)
        df_sitios = wrangling.rename_places_columns(df_sitios)

        LUGAR_INTERES = input("Introduce un centro deportivo de interes")

        df_merged = wrangling.merge_dataframes(df_bicimad,df_sitios)
        min_distance = calculation.calculate_min_distance_specific(df_merged,LUGAR_INTERES)
        final_df = calculation.define_final_df(df_merged)
        final_df = calculation.rename_final_df(final_df)
        print(final_df)



    

 

        


