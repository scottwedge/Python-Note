'''Name of the Instructor 
Email of the Instructor 
Office Hours 
Number of assignments or labs 

extract the most features from the syllabi using regular expressions.

1. There will be a folder called "syllabi" (all lower case). The folder will include 100 syllabi, all in PDF format. 
2. for each syllabus in the "syllabi" folder, it will read its text (from the PDF) .
3. extract the most features 
4. create row in a pandas dataframe with all the features extracted 
5. save a csv file called features-retrieved-by-JohnSmith.csv (all lower case) that has 100 rows,  each containing the features extracted.  Replace the JohnSmith with your name.
'''
import  PyPDF2
import pandas
import os

g = os.walk(r"C:/Users/Novogene/Documents/GitHub/Python-Note/my script/useful_script/syllabi")
for path, dir_list, file_list in g:
    for file_name in file_list:
        #print(os.path.join(path, file_name))
        print(file_name)
        
class PDF_TO_CSV(object):
    def __init__(self, filename):
        self.filename = filename
        self.feature_dict = {}
    def Open_pdf(self,filename):
        
    pdfFileobj = open('.\syllabi/13205.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
    pdfReader.numPages
    for pages in range(pdfReader.numPages):
        print(pages)
        pageObj = pdfReader.getPage(pages)
        print(pageObj.extractText())


