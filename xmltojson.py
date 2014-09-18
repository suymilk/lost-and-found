import json
import urllib
import xml.etree.ElementTree as ET

url = "http://advisory.mtanyct.info/LPUWebServices/CurrentLostProperty.aspx"
url_content = urllib.urlopen(url).read() # read content from the url 
root = ET.fromstring(url_content) # get root node

categories = [] # list of categories of lost/found items
d = { # dictionary of categories, subcategories and their counts
	"name": "All Lost Property",
	"children": []
	} 

dCh = d["children"] 

# for each category of items, create a dictionary with the category as the keys and set the category's children nodes (item, count of item) as their values
for children in root:
	tag = children.attrib.get(children.tag)
	if children.tag == "Category":
		dCh.append({"category": tag, "children": []}) # create new sub-dictionary for every new category
		for i in range(len(dCh)):
			dChCh = dCh[i]["children"] # in which the children is made up of sub-sub-dictionaries including the item and the count
		for child in children:
			dChCh.append({"item": child.attrib["SubCategory"], "count": child.attrib["count"]})

# json-fy everything
json_input = json.dumps(d, indent = 4, separators = (',', ": "))

# print json-fied content to an actual json file
json_output = open("lostandfound.json", "w")
print >>json_output, json_input

