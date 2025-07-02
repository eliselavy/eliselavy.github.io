import pandas as pd
import folium
from dotenv import load_dotenv
import os

# take the key from file .env


load_dotenv()
API_KEY = os.getenv("API_KEY")
location = "danse_sauvage_data.csv"
dance_station_locations = pd.read_csv(location)

dance_station_locations = dance_station_locations[
    ["main_place", "meeting_point", "latitude", "longitude", "date","url"]
]

# alidade smooth
# https://docs.stadiamaps.com/map-styles/alidade-smooth/

# stamen watercolor
# https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg

# stamen outdoor
# https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png


# Create a map centered on the mean of the data points
center_lat = dance_station_locations['latitude'].mean()
center_lon = dance_station_locations['longitude'].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=12, 
               tiles=f'https://tiles.stadiamaps.com/tiles/stamen_terrain/{{z}}/{{x}}/{{y}}{{r}}.png?api_key={API_KEY}', 
               attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>')


for index, location_info in dance_station_locations.iterrows():
 # Create a marker
    url = location_info['url']
    popup_content = f"<b>{location_info['main_place']}</b><br>Danse sauvage: {location_info['date']}<br>"
    color = "green"
    folium.Marker(
        [location_info["latitude"], location_info["longitude"]],
        icon=folium.Icon(color=color, icon='tree-deciduous'),
        popup=popup_content,
    ).add_to(m)
m.save("dance_sauvage_terrain.html")
