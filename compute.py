import pandas as pd
import numpy as np

def compute(college, branch, sel_years, cat, clg_type, gen): #dur

    #Read in the csv files as pandas dataframes
    nit17 = pd.read_csv('static/nit2017.csv', sep = ',')
    gfti17 = pd.read_csv('static/gfti2017.csv', sep = ',')
    iiit17 = pd.read_csv('static/iiit2017.csv', sep = ",")

    nit18 = pd.read_csv('static/nit2018.csv', sep = ',')
    gfti18 = pd.read_csv('static/gfti2018.csv', sep = ',')
    iiit18 = pd.read_csv('static/iiit2018.csv', sep = ",")

    #Some formatting to be done


    lists = []# array of original dataframes
    if("2017" in sel_years):
        if(clg_type=="nit"):
            lists.append(nit17)
        elif(clg_type=="iiit"):
            lists.append(iiit17)
        elif(clg_type=="gfti"):
            lists.append(gfti17)
    if("2018" in sel_years):
        if(clg_type=="nit"):
            lists.append(nit18)
        elif(clg_type=="iiit"):
            lists.append(iiit18)
        elif(clg_type=="gfti"):
            lists.append(gfti18)
   
    
    tableviews = [] # an array of pandas series
    results = [] # an array of pandas dataframes

    #---------------------------------------------------------------------------------------------
    
    #Filter by all the criteria
    if(college != ''):
        college_key = college.split()[-1].capitalize()
    else:
        college_key=''

    #run all the checks
    index = 0
    for list1x in lists:
        clg_check = list1x['Institute'].str.contains(college_key)

        #creating temporary series to run case insensitive checks
        temp1x = pd.Series(list1x['Academic Program Name'], dtype="str")
        temp1x = temp1x.str.replace(' ','')
        temp1x = temp1x.str.lower()

        branch_check = temp1x.str.contains(branch.lower().replace(' ','')) 
        #dur_check = list1x['Academic Program Name'].str.contains(dur) 

        if(cat!=''):
            print(cat)
            cat_check =  list1x['Seat Type'].str.contains(cat) 
        
        if(gen!=''):
            print(gen)
            gen_check = list1x['Gender'].str.contains(gen)
    
        
        tableviews.append( clg_check & branch_check & cat_check & gen_check) #dur_check
        index = index+1
   
    for i in range (0, len(lists)):
        results.append(lists[i][tableviews[i]])

    
    #---------------------------------------------------------------------------------------------
    #Convert results tables to html text
    for i in range(0, len(lists)):
        results[i] = results[i].to_html(index=False)

    return results



