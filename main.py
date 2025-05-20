import pandas as pd
import geopandas as gpd
from src.utils import create_polygon, create_city_geometries
from src.plot_map import plot_map

def main():
    print("[INFO] Veri yükleniyor...")
    cities_df = pd.read_csv('data/cities.csv')

    print("[INFO] Geometriler oluşturuluyor...")
    cities_gdf = create_city_geometries(cities_df)

    # 🔥 CRS düzeltme (centroid için gerekli)
    cities_gdf = cities_gdf.to_crs(epsg=4326)  # Asıl gösterim için yine EPSG:4326

    print("[INFO] Harita çiziliyor...")
    plot_map(cities_gdf, 'data/110m_cultural/ne_110m_admin_0_countries.shp')

if __name__ == "__main__":
    main()
