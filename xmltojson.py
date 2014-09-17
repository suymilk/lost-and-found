# from xml.dom import minidom
import xml.etree.ElementTree as ET
import urllib

url = "http://advisory.mtanyct.info/LPUWebServices/CurrentLostProperty.aspx"
url_content = urllib.urlopen(url).read()

root = ET.fromstring(url_content)

categories = []
d = {}

for children in root:
	if children.tag == "Category":
		for child in children:
			d[children.attrib.get(children.tag)] = child.attrib


print d


# json = open("lostandfound.json", "w")
# print >>json, e

