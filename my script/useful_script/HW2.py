'''
class:ANLT-224
author: Qingnan Zeng
date:0125/2020
'''
import pandas as pd
import os
import re
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *


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
                "the path" + str(self.foldername) + "you input can not be found, please correct it!")
        #return self.file_list
    @classmethod
    def search_result_correct(self, search_mod, text, group_num:int):
        try:
            x = search_mod.search(text).group(group_num)
            return x
        except AttributeError as e:
            return ''

    def Search_feature(self,filename: str):
        pdfFileobj = open(os.path.join(
            self.cwd, self.foldername, filename), 'rb')
        #create PDF interpreter based on file
        parser = PDFParser(pdfFileobj)
        # create PDF document
        document = PDFDocument(parser)
        # create PDF resourceManager
        rsrcmgr = PDFResourceManager(caching=False)
        # create PDF device
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # create interpreter
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        #create empty list
        self.email_list = []
        self.phone_list = []
        self.name_list = []
        self.website_list = []
        self.office_hour = []
        self.time_list = []
        self.course_number = []
        self.date_list = []
        self.letter_grade = []
        
        # set up the regax
        replace = re.compile(r'\s+')
        email_mod = re.compile(r'(\w+(\.\w+)*@\w+(\.\w+)*)')
        phone_mod = re.compile(r'((\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}))')
        name_regax = re.compile(r'((Professor:|Professor|Instructor:|Instructor\(s\):|Names:|Instructor.s Name)\s+(([A-Z]\w+\s+){0,2}))')
        website_regax = re.compile(r'((http|ftp|https|www)://\S+)')
        office_hour_regax = re.compile(r'([M,m]on|[T,t]ue|[W,w]ed|[T,t]hu|[F,f]ri)')
        time_regax = re.compile(r'\d+:\d+\W+\d+:\d+')
        date_regax = re.compile(r'(\d{1,2}/\d{1,2})')
        letter_grade_regax = re.compile(r'(^[A-F]|[A-F]\W)')
        course_regax = re.compile(r'(([A-Z]\w+\s+)+University|University of ([A-Z]\w+\s+)+)')

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # get the result and PDF
            self.layout = device.get_result()
            # layout including LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal and etc
            str_text = ''
            for x in self.layout:
                # only check the horizontal box
                if(isinstance(x, LTTextBoxHorizontal)):
                    #subsitute all blank and \r and \n
                    text = re.sub(replace, ' ', x.get_text())
                    str_text += text
            # print(str_text)
            self.email_list.append(PDF_TO_CSV.search_result_correct(email_mod, str_text, 0))
            self.phone_list.append(PDF_TO_CSV.search_result_correct(phone_mod, str_text, 0))
            self.name_list.append(PDF_TO_CSV.search_result_correct(name_regax, str_text, 3))
            self.website_list.append(PDF_TO_CSV.search_result_correct(website_regax, str_text, 0))
            self.office_hour.append(office_hour_regax.findall(str_text))
            self.time_list.append(time_regax.findall((str_text)))
            self.course_number.append(PDF_TO_CSV.search_result_correct(course_regax, str_text, 0))
            self.date_list.append((date_regax.findall(str_text)))
            self.letter_grade.append(letter_grade_regax.findall(str_text))

            #delete the repeat value
            self.email_list =[x for x in self.email_list if x != '']
            self.phone_list = [x for x in self.phone_list if x != '']
            self.name_list = [x for x in self.name_list if x != '']
            self.website_list = [x for x in self.website_list if x != '']
            self.office_hour = [x for x in self.office_hour if (x != '' and x != [])]
            self.time_list = [x for x in self.time_list if (x != '' and x != [])]
            self.course_number = [x for x in self.course_number if (x != '' and x != [])]
            self.date_list = [x for x in self.date_list if (x != '' and x != [])]
            self.letter_grade = [x for x in self.letter_grade if (x != '' and x != [])]

        return self.email_list, self.phone_list, self.name_list, self.website_list, self.office_hour, self.time_list, self.course_number, self.date_list, self.letter_grade
    def data_frame(self):
        df = []
        for files in self.file_list:
            if re.search(r'.*.pdf$', files):
                try:
                    features = self.Search_feature(files)
                except TypeError as e:
                    pass
            df.append({"filename": files, "email": features[0], "phone": features[1], "Professor_name": features[2],"url": features[3], "Office hours": features[4], "Time_period": features[5], "University": features[6], "Date": features[7], "Grade_level": features[8]})
        self.output_df = pd.DataFrame(df)
        self.output_df.to_csv("features-retrieved-by-QingnanZeng.csv")
            
# main script
if __name__ == "__main__":
    test = PDF_TO_CSV()
    test.Read_filename("syllabi")
    test.data_frame()