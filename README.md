
# 🗺️ City Boundary Map of Turkey

A Python project that geometrically draws and visualizes city boundaries in Turkey.

## 📦 Features

- Reads city corner coordinates from a CSV file to create polygons.
- Draws the Turkey map using a Shapefile (.shp).
- Displays city names centered on their polygons.
- Advanced error handling and stylish design.
- Modular structure suitable for GitHub projects.

## 🔧 Installation

```bash
git clone https://github.com/username/city-boundary-map.git
cd city-boundary-map
pip install -r requirements.txt
python main.py
```

## 📁 Input Format (`cities.csv`)

| pn      | southwest_lat | southwest_lon | northeast_lat | northeast_lon |
|---------|----------------|----------------|----------------|----------------|
| Ankara  | 39.5           | 32.5           | 40.1           | 33.1           |

## 🧙‍♂️ Usage

```bash
python main.py
```

The program uses `cities.csv` and `ne_110m_admin_0_countries.shp` files located in the `data/` folder to visualize the map.

## 🎯 Sample Image

![Map Sample](assets/demo.png)

## 📁 Project Structure

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

## 👨‍💻 Developer

This project is developed by [Hakan Kaygusuz](https://github.com/hakankygsz).  
Feel free to contribute via pull requests 👊

## 🧾 License

MIT License
