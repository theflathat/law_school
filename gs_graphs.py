# coding: utf-8
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import folium
import seaborn as sns
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import numpy as np
import operator

stats = pd.read_csv('/Users/heatherbaier/Desktop/law_school/conat_gs_final.csv')

stats_graph = stats.plot(x = 'Reporting Year', y = '%Total # receiving grants_all',                                   figsize = (12,8), legend = False)

#Total Recieiving Grants and Scholarships Graph
import matplotlib.style as style
style.use('fivethirtyeight')

colors = ['g', 'y', 'b', 'k', 'c', 'm', 'r']

wm = stats['%Total # receiving grants_all']
x = stats['Reporting Year']
yale = stats['%Total # receiving grants_wm']

plt.plot(x,wm, color = colors[3], linewidth  = 4)
plt.plot(x,yale, color = colors[0])


plt.rcParams["figure.figsize"] = [8,8]
plt.tick_params(axis = 'both', labelsize = 15)
plt.legend(loc = 4, shadow = True)
plt.rcParams["legend.frameon"]


plt.text(x = 2010, y = 92, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2017.5, y = 31, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2010.1, y = 90,
              s = 'Percent of students recieving grants and scholarships', fontsize = 15, weight = 'bold', alpha = .85)
plt.text(y = 30, x = 2010,
              s = '   HEATHER BAIER / THE FLAT HAT' + ' ' * 87 +  \
              'Source: American Bar Association    ', \
              fontsize = 10, color = '#f0f0f0', backgroundcolor = 'grey', fontname="Arial")
plt.show()

#Less than Half Tuition Graph
import matplotlib.style as style
style.use('fivethirtyeight')

colors = ['g', 'y', 'b', 'k', 'c', 'm', 'r']

wm = stats['% Total Less than 1/2 tuition wm']
x = stats['Reporting Year']
yale = stats['% Total Less than 1/2 tuition_all']

plt.plot(x,wm, color = colors[3], linewidth  = 4)
plt.plot(x,yale, color = colors[0])

plt.rcParams["figure.figsize"] = [8,8]
plt.tick_params(axis = 'both', labelsize = 15)
plt.legend(loc = 4, shadow = True)
plt.rcParams["legend.frameon"]


plt.text(x = 2010.2, y = 72, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2017.5, y = 28, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2010.3, y = 71,
              s = 'Percent of students recieving less than half tuition in G&S', fontsize = 15, weight = 'bold', alpha = .85)
plt.show()

#Half to Full Tuition Graph
import matplotlib.style as style
style.use('fivethirtyeight')

colors = ['g', 'y', 'b', 'k', 'c', 'm', 'r']

wm = stats['%Total Half to full tuition wm']
x = stats['Reporting Year']
yale = stats['%Total Half to full tuition all']

plt.plot(x,wm, color = colors[3], linewidth  = 4)
plt.plot(x,yale, color = colors[0])


plt.rcParams["figure.figsize"] = [8,8]
plt.tick_params(axis = 'both', labelsize = 15)
plt.legend(loc = 4, shadow = True)
plt.rcParams["legend.frameon"]


plt.text(x = 2010.2, y = 25.3, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2017.5, y = 10.9, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2010.3, y = 26,
              s = 'Percent of students recieving half to full tuition in G&S', fontsize = 15, weight = 'bold', alpha = .85)
plt.show()

#Full Tuition Graph
import matplotlib.style as style
style.use('fivethirtyeight')

colors = ['g', 'y', 'b', 'k', 'c', 'm', 'r']

wm = stats['%Total Full tuition wm']
x = stats['Reporting Year']
yale = stats['%Total Full tuition all']

plt.plot(x,wm, color = colors[3], linewidth  = 4)
plt.plot(x,yale, color = colors[0])


plt.rcParams["figure.figsize"] = [8,8]
plt.tick_params(axis = 'both', labelsize = 15)
plt.legend(loc = 5, shadow = True)
plt.rcParams["legend.frameon"]


plt.text(x = 2010.2, y = 6.2, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2017.5, y = -0.5, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2010.3, y = 6,
              s = 'Percent of students recieving full tuition in G&S', fontsize = 15, weight = 'bold', alpha = .85)
plt.show()

#More than Full Tuition Graph
import matplotlib.style as style
style.use('fivethirtyeight')

colors = ['g', 'y', 'b', 'k', 'c', 'm', 'r']

wm = stats['%Total More than full tuition wm']
x = stats['Reporting Year']
yale = stats['%Total More than full tuition all']

plt.plot(x,wm, color = colors[3], linewidth  = 4)
plt.plot(x,yale, color = colors[0])


plt.rcParams["figure.figsize"] = [8,8]
plt.tick_params(axis = 'both', labelsize = 15)
plt.legend(loc = 5, shadow = True)
plt.rcParams["legend.frameon"]


plt.text(x = 2010.2, y = 3.0, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2017.5, y = 1.45, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2010.3, y = 2.9,
              s = 'Percent of students recieving more than full tuition in G&S', fontsize = 15, \
             weight = 'bold', alpha = .85)
plt.text(y = -0.4, x = 2010.2,
              s = '   HEATHER BAIER / THE FLAT HAT' + ' ' * 82 +  \
              'Source: American Bar Association    ', \
              fontsize = 10, color = '#f0f0f0', backgroundcolor = 'grey', fontname="Arial")
plt.show()

