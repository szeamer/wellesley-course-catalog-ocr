#Silvia Zeamer
#1/25/2021

import os
import re

date_range = range(1875,2008)
dates_we_have = []
for file in os.scandir("transcripts_by_date"):
    date = re.search(r'\d{4}', file.name).group()
    dates_we_have.append(int(date))

for date in date_range:
    if date not in dates_we_have:
        print(date)