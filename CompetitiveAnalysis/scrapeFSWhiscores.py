# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:29:15 2023

@author: trevb
"""
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib3
import time

# This script scrapes the runescape FSW hiscores. The counter 'i' picks the 
# skill and 'j' picks the page of the hiscores. 

# I ran this code in snipets in a terminal. I've put it all here in what should
# work as a single script, but I haven't run this.

# While scraping, I was often rate limited. Jagex doesn't specify any rates, so 
# I tried to run at a rate that would let me scrape for a while, but that also 
# didn't make the process take days. I think it ended up taking ~4 hours, but 
# that was over 3 or 4 sessions since I got rate limited each time. I think I 
# started at waiting 2 seconds and then moved up to 4, but I'm not 100% sure.

baseurl = "https://secure.runescape.com/m=hiscore_seasonal/snapshot?category_type=0&table="
baseurl2 = "&page="
df = pd.DataFrame()
http = urllib3.PoolManager()

for i in range(0,29):
    for j in range(1,100):
        url = url = baseurl + str(i) + baseurl2 + str(j)
        response = http.request('GET',url)
        soup = BeautifulSoup(response.data)
        table = soup.find_all('table')[1]
        moredf = pd.read_html(str(table))[0]
        moredf['Category'] = i
        df = df.append(moredf)
        time.sleep(4) # Don't want to get rate limited.
        if j % 10 == 0:
            print(f'Completed i = {i} and j = {j}')
            
hiscores_map = {0:'Overall', 1:'Attack', 2:'Defence', 3:'Strength', 4:'Constitution', 5:'Ranged', 6:'Prayer', 7:'Magic', 8:'Cooking', 9:'Woodcutting', 10:'Fletching', 11:'Fishing', 12:'Firemaking', 13:'Crafting', 14:'Smithing', 15:'Mining', 16:'Herblore', 17:'Agility', 18:'Thieving', 19:'Slayer', 20:'Farming', 21:'Runecrafting', 22:'Hunter', 23:'Construction', 24:'Summoning', 25:'Dungeoneering', 26:'Divination', 27:'Invention', 28:"Archaeology"}
# This changes the numeric category to the actual skill name. It hasn't been
# run in this script file, so use at your own risk.
df['Category'] = df['Category'].map(hiscores_map)
