
# 🗺️ City Boundary Map of Turkey

Türkiye'deki şehir sınırlarını geometrik olarak çizip görselleştiren bir Python projesi.

## 📦 Özellikler

- CSV dosyasından şehir köşe koordinasyonlarını okuyarak çokgen oluşturur.
- Shapefile (.shp) ile Türkiye haritasını çizer.
- Şehir adlarını ortalarına yerleştirerek gösterir.
- Gelişmiş hata kontrolü ve şık tasarım.
- Modüler yapıda, GitHub projelerine uygun.

## 🔧 Kurulum

```bash
git clone https://github.com/kullanici-adi/city-boundary-map.git
cd city-boundary-map
pip install -r requirements.txt
python main.py
```

## 📁 Girdi Formatı (`cities.csv`)

| pn      | southwest_lat | southwest_lon | northeast_lat | northeast_lon |
|---------|----------------|----------------|----------------|----------------|
| Ankara  | 39.5           | 32.5           | 40.1           | 33.1           |

## 🧙‍♂️ Kullanım

```bash
python main.py
```

Program `data/` klasöründeki `cities.csv` ve `ne_110m_admin_0_countries.shp` dosyalarını kullanarak haritayı görselleştirir.

## 🎯 Örnek Görsel

![Harita Görseli](assets/demo.png)

## 📁 Proje Yapısı

```
city-boundary-map/
├── data/
│   ├── cities.csv
│   └── ne_110m_admin_0_countries.shp
├── src/
│   ├── __init__.py
│   ├── utils.py
│   └── plot_map.py
├── requirements.txt
├── README.md
└── main.py
```

## 👨‍💻 Geliştirici

Bu proje [Hakan Kaygusuz](https://github.com/hakankygsz) tarafından geliştirilmiştir.  
Katkıda bulunmak istersen pull request atabilirsin 👊

## 🧾 Lisans

MIT License
