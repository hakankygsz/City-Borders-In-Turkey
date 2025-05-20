import geopandas as gpd
import matplotlib.pyplot as plt

def plot_map(cities_gdf, turkey_shapefile_path):
    # Türkiye haritasını yükle
    turkey_map = gpd.read_file(turkey_shapefile_path)
    turkey_map = turkey_map[turkey_map['ADMIN'] == 'Turkey']

    # Harita çizimi
    fig, ax = plt.subplots(figsize=(14, 10))
    turkey_map.boundary.plot(ax=ax, color='black', linewidth=1)

    # Centroid hesaplamasını kopyaya yap, orijinali bozma
    cities_gdf = cities_gdf.copy()

    # PROJEKSİYON yap (EPSG:3857) — düzlem koordinatları
    projected = cities_gdf.to_crs(epsg=3857)
    projected['centroid'] = projected.geometry.centroid

    # Eski sistemle (EPSG:4326) eşitle
    cities_gdf['centroid'] = projected['centroid'].to_crs(epsg=4326)

    cities_gdf.boundary.plot(ax=ax, edgecolor='red', linewidth=1)

    for x, y, name in zip(cities_gdf['centroid'].x, cities_gdf['centroid'].y, cities_gdf['pn']):
        ax.text(
            x, y, name,
            fontsize=8, ha='center', va='center', color='blue',
            bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.2')
        )

    ax.set_title("City Borders in Turkey", fontsize=16)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    plt.tight_layout()
    plt.show()