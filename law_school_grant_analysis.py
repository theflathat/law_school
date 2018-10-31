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


gs_2011 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2011_Grants_and_Scholarships_(prior_academic_year).csv')
gs_2012 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2012_Grants_and_Scholarships_(prior_academic_year).csv')
gs_2013 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2013_Grants_and_Scholarships_(prior_academic_year).csv')
gs_2014 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2014_Grants_and_Scholarships_(prior_academic_year).csv')
gs_2015 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2015_Grants_and_Scholarships_(prior_academic_year).csv')
gs_2016 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2016_Grants_and_Scholarships_(prior_academic_year).csv')
gs_2017 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2017_Grants_and_Scholarships_right_columns.csv')


gs = pd.concat([gs_2011, gs_2012, gs_2013, gs_2014, gs_2015, gs_2016, gs_2017], axis=0, join = 'inner')


gs.to_csv('all_years_grants_and_scholarships.csv')


gs['%Total # receiving grants'].describe()


wm_gs = gs[gs['School Name'] == 'WILLIAM AND MARY LAW SCHOOL']

gs.groupby(['Reporting Year','school list'])['More than full tuition FT #'].mean()



total_grants_wm = wm_gs.groupby('Reporting Year')['%Total # receiving grants'].mean()
total_grants_all = gs.groupby('Reporting Year')['%Total # receiving grants'].mean()


less_than_half_all = gs.groupby('Reporting Year')['% Total Less than 1/2 tuition'].mean()
less_than_half_wm = wm_gs.groupby('Reporting Year')['% Total Less than 1/2 tuition'].mean()


half_to_full_all = gs.groupby('Reporting Year')['%Total Half to full tuition'].mean()
half_to_full_wm = wm_gs.groupby('Reporting Year')['%Total Half to full tuition'].mean()


more_than_full_all = gs.groupby('Reporting Year')['%Total More than full tuition'].mean()
more_than_full_wm = wm_gs.groupby('Reporting Year')['%Total More than full tuition'].mean()


full_all = gs.groupby('Reporting Year')['%Total Full tuition'].mean()
full_wm = wm_gs.groupby('Reporting Year')['%Total Full tuition'].mean()


concat_all = pd.concat([total_grants_all, total_grants_wm, less_than_half_all, less_than_half_wm, half_to_full_all, half_to_full_wm, full_all, full_wm, more_than_full_all, more_than_full_wm], axis=1)


concat_all.to_csv('concat_gs.csv')
