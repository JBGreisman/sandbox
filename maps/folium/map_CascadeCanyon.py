import folium
from xml.dom import minidom
import numpy as np
import sys

#----------------------------------------------------------------------#
# Read in XML file from RunKeeper and return the [lat lon] coordinates

def map_hike(infile):
    xmldoc = minidom.parse(infile)
    itemlist = xmldoc.getElementsByTagName('trkpt')
    coordinates = [ [float(entry.getAttribute('lat')), 
                     float(entry.getAttribute('lon'))] 
                    for entry in itemlist ]
    return np.array(coordinates)

#----------------------------------------------------------------------#

if __name__ == "__main__":

    hike = map_hike(sys.argv[1])
    avg = np.mean(hike, axis=0)
    print avg.tolist()
    map = folium.Map(location=avg.tolist(),
                     tiles='Stamen Terrain',
                     zoom_start=13)
    map.line(locations=hike, line_color="red")
    map.create_map("hike_CascadeCanyon.html")
