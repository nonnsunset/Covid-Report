import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.ticker as mtick
from numpy.polynomial.polynomial import polyfit
from gen_data import info

data, average = info()
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()

