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

  
class PDF_TO_CSV(object):
    def __init__(self):
        self.file_list = []
        self.feature_dict = {}
        self.foldername = ""
        self.cwd = ""
    
    def Read_filename(self, foldername: str) -> list:
        self.cwd = os.getcwd()
        self.foldername = foldername
        try:
            self.file_list = os.listdir(os.path.join(os.getcwd(), self.foldername))
        except FileNotFoundError as e:
            raise FileNotFoundError(
                "the path" + str(path) + "you input can not be found, please correct it!")
        return self.file_list
    
    def Open_pdf(self,filename: str):
        pdfFileobj = open(os.path.join(self.cwd, self.foldername, filename), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
        pdfReader.numPages
        for pages in range(pdfReader.numPages):
            print(pages)
            pageObj = pdfReader.getPage(pages)
            print(pageObj.extractText())


# main script
test = PDF_TO_CSV()
filename_list = test.Read_filename("syllabi")
