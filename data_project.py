###################################  project #########################################


# needed modules :


import re       
import os        
import requests

# needed functions :

def max(lsts):
    max=lsts[0]
    for item in lsts:
        if item>max:
            max=item
    return max

def cleaning(lst_words):
    lst_tamiz=[]
    for item in lst_words :
        g=''
        for char in item:
            if char not in '!@#$%^>?,':
                g=g+char
        lst_tamiz.append(g)
    return lst_tamiz

def tekrari(lst_x):
    lst_tekrari=[]
    lst_output=[]
    for item in lst_x:
        if item not in lst_tekrari:
            lst_output.append(item)
            lst_tekrari.append(item)
    return lst_output

#---------------------------------------------    
# open a folder for saving data :

os.mkdir('E:\ project data')
os.chdir('E:\ project data')
#---------------------------------------------
# finding countrys names :

name_of_counrtie_dirty=[]
lst_contients=['https://www.worlddata.info/america/index.php','https://www.worlddata.info/europe/index.php','https://www.worlddata.info/asia/index.php','https://www.worlddata.info/africa/index.php','https://www.worlddata.info/australia/index.php']

for item in lst_contients:
    response=requests.get(item)
    text=response.text
    all_countries_in_contient=re.findall(r'href=\S{14,45}', text)
    
    for item in all_countries_in_contient:
        name_of_counrtie_dirty.append(item)

lst_countries=[]
for item_1 in name_of_counrtie_dirty:
    g=''
    lst_words=[]
    for item_2 in item_1:
        if item_2 not in '/':
            g=g+item_2
                
        if item_2=='/':
            lst_words.append(g)
            g=''
    if len(lst_words)>2:
        if lst_words[1]=='america' or lst_words[1]=='europe' or lst_words[1]=='asia' or lst_words[1]=='africa' or lst_words[1]=='australia':
            lst_countries.append(lst_words[1]+'/'+lst_words[2])


lst_only_countries=[]
for item in tekrari(lst_countries):
    g=''
    for char in item:
        if char!='/':
                g=g+char
        elif char=='/':
            g=''
    lst_only_countries.append(g)
    

countries_name_data=open('countries_name.txt','a')
for item in lst_only_countries:
    o=open(f'{item}.txt','a')
    countries_name_data.write(f'{item} \n')
    o.write(item+'\n')


    

#---------------------------------------------

# sending request to countries pages :


# 1 : finding population 

for item_3 in tekrari(lst_countries):
    response_1=requests.get(f'https://www.worlddata.info/{item_3}/index.php').text
    country_population=re.findall(r'>Population:</a>\S{,15}',response_1)
    if len(country_population)>0:
        countries_population=''
        for item in country_population[0]:
            if item in '0987654321':
                countries_population=countries_population+item

    elif len(country_population)==0:
        countries_population='0'    
    
    g=''
    for char in item_3:
        if char!='/':
            g=g+char
        elif char=='/':
            g=''
    o=open(f'{g}.txt','a')
    o.write(countries_population+'\n')

# 2 : finding GDP 

    country_gdp=re.findall(r'<td>GDP:</td><td>\S{1,10} bn',response_1)
    if len(country_gdp)>0:
        countries_gdp=''
        for item in country_gdp[0]:
            if item in '0987654321':
                countries_gdp=countries_gdp+item
            elif item=='.':
                break
        countries_gdp=str(int(countries_gdp)*10**9)
    
    if len(country_gdp)==0:
        country_gdp_m=re.findall(r'<td>GDP:</td><td>\S{1,8} M', response_1)
        if len(country_gdp_m)>0:
            countries_gdp=''
            for item in country_gdp_m[0]:
                if item in '0987654321':
                    countries_gdp=countries_gdp+item
                elif item=='.':
                    break
        if len(country_gdp_m)==0:
            countries_gdp='0'
        countries_gdp=str(int(countries_gdp)*10**6)

    o.write(countries_gdp+'\n')

# 3 finding the birth to death ratio (birthrate/deathrate)       
    
    country_birthrate=re.findall(r'<div>Birthrate:</div>\S{,7}',response_1)
    country_birthrate_clean=''
    if len(country_birthrate)>0:
        for item in country_birthrate[0]:
            if item in '0987654321.':
                    country_birthrate_clean=country_birthrate_clean+item
    elif len(country_birthrate)==0:
        country_birthrate_clean='0'    
        
    country_deathrate=re.findall(r'<div>Deathrate:</div>\S{,7}',response_1)
    country_deathrate_clean=''
    if len(country_deathrate)>0:
        for item in country_deathrate[0]:
            if item in '0987654321.':
                    country_deathrate_clean=country_deathrate_clean+item      
    elif len(country_deathrate)==0:
        country_deathrate_clean='0'
    
    vasiat_jamiiat=((int(float(country_birthrate_clean))-int(float(country_deathrate_clean))))
    
    o.write(str(vasiat_jamiiat))
    
# 4 and 5 : finding life hope for man and women
    
    # country_life_hope=re.findall(r'\S{,5} years',response_1)
    # if len(country_life_hope)>0:
    #     g_hope_man=''
    #     for char in country_life_hope[0]:
    #         if char in '0123456789.': 
    #             g_hope_man=g_hope_man+char
    # if len(country_life_hope)>0:
    #     g_hope_women=''
    #     for char in country_life_hope[1]:
    #         if char in '0123456789.':
    #             g_hope_women=g_hope_women+char
    # if len(country_life_hope)==0:
    #     g_hope_man='0'
    #     g_hope_women='0'
    
    # o.write('\n'+g_hope_man+'\n')
    # o.write(g_hope_women+'\n')

# 6 :

#     country_exportation=re.findall(r'<td>Exportations:</td><td>\S{,10} bn',response_1)
#     g_expo=''
#     if len(country_exportation)>0:
#         for item in country_exportation[0]:
#             if item in '0987654321':
#                 g_expo=g_expo+item
#         g_expo=int(float(g_expo))*10**9
#     elif len(country_exportation)==0:
#         country_exportation=re.findall(r'<td>Exportations:</td><td>\S{,10} M',response_1)
#         if len(country_exportation)==0:
#             g_expo='0'
#         if len(country_exportation)>0:
#             for item in country_exportation[0]:
#                 if item in '0987654321':
#                     g_expo=g_expo+item
#         g_expo=int(float(g_expo))*10**6
#     o.write(str(g_expo)+'\n')

# # 7 :

#     country_ppk=re.findall(r'Population per km²:</a>\S{3,9}',response_1)
#     g_ppk=''
#     if len(country_ppk)>0:
#         for item in country_ppk[0]:
#             if item in '0987654321.':
#                 g_ppk=g_ppk+item
#     if len(country_ppk)==0:
#         g_ppk='0'
#     o.write(g_ppk+'\n')

# # 8 :
    
#     country_tour=re.findall(r'Tourism receipts</a>:</td><td>\S{1,6}',response_1)
#     g_tour=''
#     if len(country_tour)>0:
#         for item in country_tour[0]:
#             if item in '0987654321.':
#                 g_tour=g_tour+item
#     if len(country_tour)==0:
#         g_tour='0'
#     o.write(g_tour+'\n')

# print('extraction completed !')