	#!/usr/bin/python3

		import convertCSVtoDict.py
		import pandas as pd
		import json, glob, os
		
		
		json_path = 'C:\Users\gregory_majersky\Documents\MergedCSVs\mergedpandas_asjson'
		
		#list all files to be processed
		json_files = os.listdir(json_path)
		
		json_join = os.path.join(json_files, '*.json')
		joined_list = glob.glob(json_join)
		
				
		for f in json_files:
			print("These are the files that will be processed: " + f)
		
		
		df_list = []
		
		for file in joined_list:
			with open(file) as f: 
				#reading the files with f.read() and loading them as JSON records by method json.loads, and create a Pandas DataFrame
				json_data = pd.json_normalize(json.loads(f.read()))   
				json_data['site'] = file.rsplit("/", 1)[-1]  #gives a trace of each record from which file is coming
			df_list.append(json_data)
		df = pd.concat(df_list)   #concatenating list of DataFrames into a single one
		
		
		
		
	