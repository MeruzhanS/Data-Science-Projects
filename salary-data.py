import json  
# Opening JSON file
f = open('/Users/meruzhansargsyan/Desktop/Data Science Projects/Salary-Data.json')
  
# retuns JSON object as 
# a dictionary
data = json.load(f)
sample = data["Sheet 1 - salary_data"]
#creating a new dictionary
newDict = {}
current = 0
#creating a new json file
out_file = open("Salary-Data-2.json", "w")

#place education level of 2 in newDict
for i in sample:
    if i.get("education_level", None) != "2":
        del i
        continue
    if i["age"] < "40":
        i["color"] = "pink"
    elif i["age"] >= "40":
        i["color"] = "black"
    newDict[current] = i
    current += 1

#make new file using newDict
json.dump(newDict, out_file, indent = 6)

# Closing file
f.close()