# from xml.dom import minidom
import xml.etree.ElementTree as ET
import urllib
import json

url = "http://advisory.mtanyct.info/LPUWebServices/CurrentLostProperty.aspx"
url_content = urllib.urlopen(url).read()

root = ET.fromstring(url_content)

categories = []
d = {}

for children in root:
	if children.tag == "Category":
		for child in children:
			d[children.attrib.get(children.tag)] = [child.attrib]

json_input = json.dumps(d, sort_keys = True, indent = 4, separators = (',', ": "))

json_output = open("lostandfound.json", "w")
print >>json_output, json_input

