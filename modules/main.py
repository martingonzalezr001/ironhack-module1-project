#Imports:
import json
from shapely.geometry import Point
import geopandas as gpd
import acquisition
import wrangling
import calculation
import timeit



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




#tiempo = timeit.timeit(calculation.calculate_min_distance, number=1)
#print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
if calculation.argument_parser().function == "Todos":
    min_distance = calculation.calculate_min_distance(df_merged)
    final_df = calculation.define_final_df(df_merged)
    final_df = calculation.rename_final_df(final_df)
    print(final_df)

if calculation.argument_parser().function == "Sitio":
    min_distance = calculation.calculate_min_distance_specific(df_merged)
    final_df = calculation.define_final_df(df_merged)
    final_df = calculation.rename_final_df(final_df)
    print(final_df)

 

        


