# Getting and cleaning data - Coursera, University Johns Hopkins University

import os
import pandas as pd
import requests
import xml.etree.ElementTree as et

from urllib.request import urlopen

# If the directory datasets doesn't exist, it will be created.
if not os.path.exists("datasets"):
    os.makedirs("datasets")

# Download the file from this url
def downloadFile(url, name, extension):
    
    with urlopen(url) as testfile, open("./datasets/" + name + extension, 'w') as f:
        f.write(testfile.read().decode())

def readLocalFiles():
    # Function that reads a local file.
    dataset = pd.read_csv("./datasets/dataset.csv", sep=",")

    print(dataset.head())

def readExcelFiles():
    # Function that reads a Excel file.
    dataset = pd.read_excel("./datasets.dataset.xlsx")

# Source: https://docs.python.org/2/library/xml.etree.elementtree.html 
def readXMLFiles():

    tree = et.parse('./datasets/dataset.xml')
    root = tree.getroot()

def readJSON():
	
	import json
	
	# Open the json file
	with open("datasets/dataset.json") as f:
		data = json.load(f)
		# Print the key's value
		print(data[0]["id"])

# Source: https://www.tutorialspoint.com/python3/python_database_access.htm
#		  https://stackoverflow.com/questions/3556305/how-to-retrieve-table-names-in-a-mysql-database-with-python-and-mysqldb
#    	  https://stackoverflow.com/questions/23786674/python-mysqldb-how-to-get-columns-name-without-executing-select-in-a-big-tab
def readMySQL(url, user, password):

	import pymysql

	db = pymysql.connect(url, user, password)

	cursor = db.cursor()

	# Show all the datatbases
	cursor.execute("show databases")
	for databases in cursor:
		print(databases[0])
 
	# Show all the tables from database "hg19"
	cursor.execute("use hg19")
	cursor.execute("show tables")
	for tables in cursor:
		print(tables[0])

	# Show the columns from table affyU133Plus2
	cursor.execute("show columns from affyU133Plus2")
	for names in cursor:
		print(names)

	# Show all data from table affyU133Plus2
	cursor.execute("select * from affyU133Plus2")
	for names in cursor:
		print(names)

	# Close the connection
	db.close()

def webScraping():

	with urlopen("https://scholar.google.com/citations?user=HI-I6C0AAAAJ&hl=en") as testfile:
		html = testfile.read().decode()

	print(html)
	tree = et.fromstring("<html><head><title>Jeff Leek - Google Scholar Citations</title></head></html>")


#url = "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
#url = "http://api.github.com/users/jtleek/repos"
#downloadFile(url, "dataset", ".csv")
#readLocalFiles()
#readXMLFiles()
#readJSON()
#readMySQL("genome-mysql.soe.ucsc.edu", "genomep", "password")
webScraping()



