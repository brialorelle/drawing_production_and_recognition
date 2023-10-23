
## basic library requirements
from __future__ import division

import os
import numpy as np
import pandas as pd

# set path to database connectinos 
auth = pd.read_csv('../auth.txt', header = None) 
pswd = auth.values[0][0]

## use pymongo for database
import pymongo as pm
conn = pm.MongoClient('mongodb://stanford:' + pswd + '@127.0.0.1')
db = conn['kiddraw']
cdm_run_v7 = db['cdm_run_v7']
cdm_run_v6 = db['cdm_run_v6']
cdm_run_v5 = db['cdm_run_v5']
cdm_run_v4 = db['cdm_run_v4']
cdm_run_v3 = db['cdm_run_v3']

##
ages = ['age2','age3','age4','age5','age6','age7','age8','age9','age10']
collections = [cdm_run_v3, cdm_run_v4, cdm_run_v5, cdm_run_v6, cdm_run_v7] 

other_draw_count=[]
parent_draw_count=[]
interference_age=[]
which_collection=[]
all_surveys_count=[]

for this_collection in collections:
    for this_age in ages:
        print(this_age)
        all_surveys = this_collection.find({'$and': [{'dataType':'survey'},{'age': this_age}]})
        other_drew = this_collection.find({'$and': [{'dataType':'survey'},{'age': this_age}, {'other_drew':True}]})
        parent_drew = this_collection.find({'$and': [{'dataType':'survey'},{'age': this_age}, {'parent_drew':True}]})
        parent_draw_count.append(parent_drew.count())
        all_surveys_count.append(all_surveys.count())
        other_draw_count.append(other_drew.count())
        interference_age.append(this_age)
        which_collection.append(this_collection)

## write out a csv with these variables
X_out = pd.DataFrame([which_collection,interference_age,parent_draw_count,other_draw_count,all_surveys_count])
X_out = X_out.transpose()
X_out.columns = ['which_collection','interference_age','parent_draw_count','other_draw_count','all_surveys_count']
X_out.to_csv(os.path.join('interference_count_across_age_and_runs.csv'))   