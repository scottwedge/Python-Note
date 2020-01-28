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

from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
import re


  
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
    
    def Regular_exp_check(self):

# main script
test = PDF_TO_CSV()
filename_list = test.Read_filename("syllabi")

fp = open(u"C:\\Users\\Novogene\\Documents\\GitHub\\Python-Note\\my script\\useful_script\\syllabi\\SPRING-2019-Biology-101-Syllabus_schedule.pdf", 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
rsrcmgr = PDFResourceManager(caching=False)
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

replace = re.compile(r'\s+')
email_mod = re.compile(r'(\w+(\.\w+)*@\w+(\.\w+)*)')

for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # 接受该页面的LTPage对象
    layout = device.get_result()
    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
    for x in layout:
        #如果x是水平文本对象的话
        if(isinstance(x, LTTextBoxHorizontal)):
            email = email_mod.findall(x.get_text())
            if len(email) != 0:
                print(email[0][0])
            #text = re.sub(replace, ' ', x.get_text())
            #if len(text) != 0:
            #    print(text)
            #    print(email)
#
