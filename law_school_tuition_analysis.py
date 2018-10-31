# coding: utf-8

#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import operator

tf_2011 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2011_Tuition_and_Fees_and_Living_Expenses.csv')
tf_2012 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2012_Tuition_and_Fees_and_Living_Expenses.csv')
tf_2013 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2012_Tuition_and_Fees_and_Living_Expenses.csv')
tf_2014 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2014_Tuition_and_Fees_and_Living_Expenses.csv')
tf_2015 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2015_Tuition_and_Fees_and_Living_Expenses.csv')
tf_2016 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2016_Tuition_and_Fees_and_Living_Expenses.csv')
tf_2017 = pd.read_csv('/Users/heatherbaier/Desktop/law_school/2017_Tuition_and_Fees_and_Living_Expenses.csv')


tf = pd.concat([tf_2011, tf_2012, tf_2013, tf_2014, tf_2015, tf_2016, tf_2017], axis=0, join = 'inner')


tf.columns = tf.columns.str.replace(' ','_')
tf.columns = tf.columns.str.replace('-','')


tf['FullTime_Resident'] = tf['FullTime_Resident'].str.replace('$','')
tf['FullTime_Resident'] = tf['FullTime_Resident'].str.replace(',','')

tf['FullTime_NonResident'] = tf['FullTime_NonResident'].str.replace('$','')
tf['FullTime_NonResident'] = tf['FullTime_NonResident'].str.replace(',','')

tf['Living_on_Campus'] = tf['Living_on_Campus'].str.replace('$','')
tf['Living_on_Campus'] = tf['Living_on_Campus'].str.replace(',','')

tf['Living_Off_Campus'] = tf['Living_Off_Campus'].str.replace('$','')
tf['Living_Off_Campus'] = tf['Living_Off_Campus'].str.replace(',','')

tf['Living_at_Home'] = tf['Living_at_Home'].str.replace('$','')
tf['Living_at_Home'] = tf['Living_at_Home'].str.replace(',','')


tf['FullTime_Resident'] = tf.FullTime_Resident.astype(int)
tf['FullTime_NonResident'] = tf.FullTime_NonResident.astype(int)


tf['Living_on_Campus'] = pd.to_numeric(tf['Living_on_Campus'], errors='coerce')
tf['Living_Off_Campus'] = pd.to_numeric(tf['Living_Off_Campus'], errors='coerce')
tf['Living_at_Home'] = pd.to_numeric(tf['Living_at_Home'], errors='coerce')


wm_tf = tf[tf['School_Name'] == 'WILLIAM AND MARY LAW SCHOOL']

tutionR_wm = wm_tf.groupby('Reporting_Year')['FullTime_Resident'].mean()
tutionR_all = tf.groupby('Reporting_Year')['FullTime_Resident'].mean()


tutionNR_wm = wm_tf.groupby('Reporting_Year')['FullTime_NonResident'].mean()
tutionNR_all = tf.groupby('Reporting_Year')['FullTime_NonResident'].mean()


tutionOC_wm = wm_tf.groupby('Reporting_Year')['Living_on_Campus'].mean()
tutionOC_all = tf.groupby('Reporting_Year')['Living_on_Campus'].mean()


tutionOFFC_wm = wm_tf.groupby('Reporting_Year')['Living_Off_Campus'].mean()
tutionOFFC_all = tf.groupby('Reporting_Year')['Living_Off_Campus'].mean()


tutionH_wm = wm_tf.groupby('Reporting_Year')['Living_at_Home'].mean()
tutionH_all = tf.groupby('Reporting_Year')['Living_at_Home'].mean()


concat_all = pd.concat([tutionR_wm, tutionR_all, tutionNR_wm, tutionNR_all, tutionOC_wm, tutionOC_all, tutionOFFC_wm, tutionOFFC_all, tutionH_wm, tutionH_all], axis=1)

concat_all.to_csv('concat_tf.csv')

