
# coding: utf-8

#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import operator

stats = pd.read_csv('/Users/heatherbaier/Desktop/law_school/tf_final.csv')

stats.columns = stats.columns.str.replace(' ','_')
stats.columns = stats.columns.str.replace('-','')

def subtract(a,b):
    new_list = []
    count = 0
    for i in a:
        val = i - b[count]
        new_list.append(val)
        count += 1
    return new_list


ftr_wm = stats['FullTime_Resident_W&M'].tolist()
ftr_all = stats['FullTime_Resident_All'].tolist()
ftnr_wm = stats['FullTime_NonResident_W&M'].tolist()
ftnr_all = stats['FullTime_NonResident_All'].tolist()
oc_wm = stats['Living_on_Campus_W&M'].tolist()
oc_all = stats['Living_on_Campus_All'].tolist()
offc_wm = stats['Living_Off_Campus_W&M'].tolist()
offc_all = stats['Living_Off_Campus_All'].tolist()
home_wm = stats['Living_at_Home_W&M'].tolist()
home_all = stats['Living_at_Home_All'].tolist()


FullTime_Resident_Difference = subtract(ftr_wm, ftr_all)
FullTime_NonResident_Difference = subtract(ftnr_wm, ftnr_all)
Living_on_Campus_Difference = subtract(oc_wm, oc_all)
Living_Off_Campus_Difference = subtract(offc_wm, offc_all)
Living_at_Home_Difference = subtract(home_wm, home_all)


stats['FullTime_Resident_Difference'].mean()


stats['FullTime_Resident_Difference'] = FullTime_Resident_Difference
stats['FullTime_NonResident_Difference'] = FullTime_NonResident_Difference
stats['Living_on_Campus_Difference'] = Living_on_Campus_Difference
stats['Living_Off_Campus_Difference'] = Living_Off_Campus_Difference
stats['Living_at_Home_Difference'] = Living_at_Home_Difference


#Final Graph on Tuition
import matplotlib.style as style
style.use('fivethirtyeight')

colors = ['g', 'y', 'b', 'k', 'c', 'm', 'r']

wm = stats['FullTime_Resident_W&M']
x = stats['Reporting_Year']
yale = stats['FullTime_Resident_All']

plt.plot(x,wm, color = colors[0], linewidth  = 4)
plt.plot(x,yale, color = colors[3])


plt.rcParams["figure.figsize"] = [8,8]
plt.tick_params(axis = 'both', labelsize = 15)
plt.legend(loc = 4, shadow = True)
plt.rcParams["legend.frameon"]


plt.text(x = 2010, y = 39500, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2017.5, y = 25000, s = '.', color ='y',              weight = 'bold', rotation = 18, backgroundcolor = '#f0f0f0', fontsize = 1)
plt.text(x = 2010.1, y = 39000,
              s = 'Full Time Residential Student Tution Between 2001 and 2017', fontsize = 15, weight = 'bold', alpha = .85)
plt.text(y = 24500, x = 2009.9,
              s = '   HEATHER BAIER / THE FLAT HAT' + ' ' * 87 +  \
              'Source: American Bar Association    ', \
              fontsize = 10, color = '#f0f0f0', backgroundcolor = 'grey', fontname="Arial")
plt.show()

