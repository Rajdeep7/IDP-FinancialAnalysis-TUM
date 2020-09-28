import pandas as pd
from summarizer import Summarizer
from pathlib import Path
import os


list_of_files=[]
# sets the path where all the reports are kept
#basepath = Path('/home/tuhin/Tuhin/Apple(Economic) Reports/')

# loops through each report to extract document information
files_in_basepath = os.scandir('/Users/rajdeepsurolia/Downloads/Apple(Economic) Reports/')
#files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
     print(item.name)
     pdf = PdfFileReader(item)

     # This takes the 1st page from a single report
     page = pdf.getPage(0)
     # This extracts the text 
     text = page.extractText()



     # This summarizes The text from page(0) which is the most important page ie the fist page from a single report
     model = Summarizer()
     result = model(text, min_length=20)
     summarized = ''.join(result)

     # creates a list of summarized files which needs to be converted to a dataframe
     list_of_files.append(summarized)








 
