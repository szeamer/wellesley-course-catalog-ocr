#Silvia Zeamer
#1/22/2021

import os
import re

try:
    os.mkdir("transcripts_by_date")
except(FileExistsError):
    print("Already made.")

for transcript in os.scandir("transcriptions"):
    print(transcript.name)
    hasMatch = False
    matches = []
    filename = ""
    with open("transcriptions/{}".format(transcript.name), "r", encoding="utf-8") as f:
        full_text = f.readlines()
        start_text = full_text[0:16]
        for line in start_text:
            line = line.replace(' ', '')
            match = re.search(r'\d{4}.*\d{2,4}', line)
            if match == None:
                match = re.search(r'\d{4}', line)
            if match != None:
                hasMatch = True
                print(match.group())
                matches.append(match.group())
                #print(line)
        if re.search(r'\d{4}[^|]*\d{2,4}', "|".join(matches)) != None:
            filename = re.search(r'\d{4}[^|]*\d{2,4}', "|".join(matches)).group()
        elif re.search(r'\d{4}', "|".join(matches)) != None:
            filename = re.search(r'\d{4}', "|".join(matches)).group()

        print("FILENAME IS " + filename)
        
        # print(match)

        with open("transcripts_by_date/{}.txt".format(filename), "w", encoding="utf-8") as date_file:
            date_file.writelines(full_text)

        



