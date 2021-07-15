#!/usr/bin/python3

import csv
import pandas as pd
import json


#request the file to be converted:
answer = input("Which file do you want to convert to a dictionary? Don't forget the file ending:  ")
print("You have requested: " + answer)


#read csv file from input
csvfile = pd.read_csv(answer, index_col = False, encoding = 'utf-8', error_bad_lines = False, sep = ';|"', engine = 'python')

#drop null value columns to avoid errors
csvfile.dropna(how = 'all', inplace = True, axis = 1)

#converting to dictionary
csv2dict = csvfile.to_dict()

#display
print(csv2dict)

#request the name of json file to be created
print(" ")
print(" ")
json_answer = input("Enter the desired name for the new json file.  Do not forget to add '.json' :   ")

#Convert to json
with open(json_answer, "w") as outfile:
	json.dump(csv2dict, outfile, ensure_ascii = True, check_circular = True, allow_nan = True, indent = 4)
	print("You have created the json file " + json_answer + ".")

outfile.close()

print(json_answer)

