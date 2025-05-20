import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

# Her şehir için dikdörtgen sınır polygon'u oluştur
def create_polygon(row):
    try:
        if row['southwest_lat'] < row['northeast_lat'] and row['southwest_lon'] < row['northeast_lon']:
            return Polygon([
                (row['southwest_lon'], row['southwest_lat']),
                (row['northeast_lon'], row['southwest_lat']),
                (row['northeast_lon'], row['northeast_lat']),
                (row['southwest_lon'], row['northeast_lat']),
                (row['southwest_lon'], row['southwest_lat'])  # kapanış noktası
            ])
        else:
            print(f"[UYARI] Geçersiz koordinatlar: {row.get('pn', 'Bilinmiyor')}")
            return None
    except Exception as e:
        print(f"[HATA] Polygon oluşturulamadı: {e}")
        return None

# GeoDataFrame oluşturur
def create_city_geometries(cities_df):
    cities_df = cities_df.copy()
    cities_df['geometry'] = cities_df.apply(create_polygon, axis=1)
    cities_df = cities_df.dropna(subset=['geometry'])  # Hatalı geometrileri at
    cities_gdf = gpd.GeoDataFrame(cities_df, geometry='geometry', crs="EPSG:4326")
    return cities_gdf
