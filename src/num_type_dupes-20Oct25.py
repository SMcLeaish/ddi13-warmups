from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt

aggdf = pd.read_csv("num_type_dupes-data-20Oct25/2011_ag.csv")

@dataclass
class PltConfig():
    title ='Total Veg Exports vs Total Fruit Exports' 
    xlabel= 'Total Veggies Exported (Tons)'
    ylabel= 'Total Fruits Exported (Tons)'
    color= 'red'
    marker= 'x'
    legend= True
    legend_label='veggies and fruits' 
config = PltConfig
plt.scatter(aggdf['total veggies'], aggdf['total fruits'], label=config.legend_label, marker=config.marker, color=config.color)
plt.title(config.title)
plt.xlabel(config.xlabel)
plt.ylabel(config.ylabel)
if config.legend:
    plt.legend()
plt.text(1900, 8600, "Outlier")