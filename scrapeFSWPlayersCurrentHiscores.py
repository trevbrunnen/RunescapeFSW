# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:56:06 2023

@author: trevb
"""
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib3
import time
from tqdm import tqdm

fsw_hiscores = pd.read_csv('./FSW_Players_CurrentHiscores_OnlyOverall_Laptop_1.csv',index_col=0)

baseurl = 'https://secure.runescape.com/m=hiscore/index_lite.ws?player='
df = pd.DataFrame()
http = urllib3.PoolManager()

already_done = fsw_hiscores.dropna()
need_to_do = fsw_hiscores[fsw_hiscores['CurrentLvl'].isna()]

for row, whatever in tqdm(need_to_do.iterrows()):
    url = baseurl + whatever['Username']
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data)
    
    try:
        newdf = pd.DataFrame(soup.get_text().split('\n')[0:29])
        newdf[['Rank','Level','Exp']] = newdf[0].str.split(',',expand = True)
    except:
        need_to_do.at[row,'CurrentLvl'] = 'Not on Hiscores'
        need_to_do.at[row,'CurrentExp'] = 'Not on Hiscores'
    else:

        newdf['Username'] = whatever['Username']
        need_to_do.at[row,'CurrentLvl'] = newdf.at[0,'Level']
        need_to_do.at[row,'CurrentExp'] = newdf.at[0,'Exp']
        
        df = df.append(newdf)
    
    time.sleep(2)