import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def draw_USA():
    """initialize a basemap centered on the continental USA"""
    plt.figure(figsize=(14, 10))
    return Basemap(projection='lcc', resolution='l',
                   llcrnrlon=-119, urcrnrlon=-64,
                   llcrnrlat=22, urcrnrlat=49,
                   lat_1=33, lat_2=45, lon_0=-95,
                   area_thresh=10000)

if __name__ == '__main__':
    
    m = draw_USA()
    
    # Draw map background
    m.fillcontinents(color='white', lake_color='#eeeeee')
    m.drawstates(color='lightgray')
    m.drawcoastlines(color='lightgray')
    m.drawcountries(color='black')
    m.drawmapboundary(fill_color='#eeeeee')
    m.shadedrelief()
    
    plt.show()
