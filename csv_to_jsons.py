import csv
import json

with open("{filepath}") as datacsv:
  dataReader = csv.DictReader(datacsv)
  i = 0
  for row in dataReader:
    output_path = "{file_output_path}" + str(i) + ".json" 
    with open(output_path, "w") as output_file:
      json.dump(row,output_file)
    i = i + 1 
