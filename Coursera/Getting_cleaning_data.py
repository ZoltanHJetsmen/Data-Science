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
    

    


url = "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
#downloadFile(url, "dataset", ".csv")
#readLocalFiles()
#readXMLFiles()




