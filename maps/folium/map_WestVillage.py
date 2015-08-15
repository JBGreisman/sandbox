import folium

map = folium.Map(location=[40.730546, -74.0038151], 
                 tiles='Stamen Toner',
                 zoom_start=17)
map.create_map("nyc_westVillage.html")
