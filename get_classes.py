#Silvia Zeamer
#1/26/2021

import re
#Format: {YEAR: {Subject:[Class, Class, Class]}}

course_dict = {}

def read_1876():
    #get the text we want
    #COURSE OF STUDY to QUALIFICATIONS FOR ADMISSION TO THE GENERAL COURSE.
    class_text = []

    with open("transcripts_by_date/1876.txt", 'r', encoding="utf-8") as f:
        all_lines = f.readlines()
        #print(all_lines)
        in_classes = 0
        boundary_lines = ["COURSE OF STUDY.", "QUALIFICATIONS FOR ADMISSION TO THE GENERAL COURSE"]

        for line in all_lines:
            #print(line)
            if boundary_lines[0] in line:
                in_classes = 1
                continue
            elif boundary_lines[1] in line:
                in_classes = 0
                continue

            if in_classes == 1:
                class_text.append(line)
    
    #extract subjects
    for line in class_text:
        subject = re.search(r'^[A-Z][a-z]*\.', line)
        if subject != None:
            print(subject.group())

    #extract classes
    for line in class_text:
        classes = re.findall(r'[A-Z][A-Za-z\s,]*;', line)
        if classes != None:
            print(classes)
    print(class_text)

read_1876()

