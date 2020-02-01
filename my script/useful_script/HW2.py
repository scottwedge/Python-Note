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
    def Search_feature(self,filename: str):
        pdfFileobj = open(os.path.join(
            self.cwd, self.foldername, filename), 'rb')  # 以二进制读模式打开
        #用文件对象来创建一个pdf文档分析器
        parser = PDFParser(pdfFileobj)
        # 创建一个PDF文档
        document = PDFDocument(parser)
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager(caching=False)
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        #创建list
        email_list = []
        phone_list = []
        name_list = []
        website_list = []
        office_hour = []
        ISBN_list = []
        course_number = []
        date_list = []
        letter_grade = []
        
        # 定义读取text的正则
        replace = re.compile(r'\s+')
        email_mod = re.compile(r'(\w+(\.\w+)*@\w+(\.\w+)*)')
        phone_mod = re.compile(r'((\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}))')
        name_regax = re.compile(r'((Professor:\s+|Instructor:*\s*)(\w+\s+|\w+\.){2,5})', re.I)
        website_regax = re.compile(r'((http|ftp|https|www)://\S+)')
        office_hour_regax = re.compile(r'(\d{2}:\d{2})')
        ISBN_regax = re.compile(r'(ISBN.*(\d+-*|\d+)+)')
        date_regax = re.compile(r'(^\d{1,2}(/|-)\d{1,2})')
        letter_grade_regax = re.compile(r'(^[A-F]|[A-F]\W)')
        course_regax = re.compile(r'(^[a-zA-Z]{3,10}[" "]\d{3,5}[" "]?[a-zA-Z]{0,1}$)')
        regax_list = {
            email_mod:email_list, phone_mod:phone_list, website_regax:website_list, office_hour_regax:office_hour,
            ISBN_regax:ISBN_list, date_regax:date_list, letter_grade_regax:letter_grade, course_regax:course_number
        }
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            for x in layout:
                #如果x是水平文本对象的话
                if(isinstance(x, LTTextBoxHorizontal)):
                    #替换所有
                    text = re.sub(replace, ' ', x.get_text())
                    try:
                        name_list.append(name_regax.search(text).group(3))
                    except:
                        pass
                    for keys in regax_list:
                        try:
                            regax_list[keys].append(keys.search(text).group(1))
                        except:
                            pass
            #得出的结果去重复
            name_list = list(filter(lambda x:name_list.count(x) == 1, name_list))
            for key in regax_list:
                regax_list[key] = list(filter(lambda x:regax_list[key].count(x) == 1, regax_list[key]))

        return email_list, phone_list, name_list, website_list, office_hour, ISBN_list, course_number, date_list, letter_grade
    def data_frame(self):
        df = []
        for files in self.file_list:
            features = self.Search_feature(files)
            df.append({"filename": files, "email": features[0], "phone": features[1], "Professor_name": features[2],"url": features[3], "Office hours": features[4], "ISBN_code": features[5], "course_code": features[6], "Date": features[7], "Grade_level": features[8]})
        self.output_df = pd.DataFrame(df)
        self.output_df.to_csv("features-retrieved-by-QingnanZeng.csv")
            
# main script
if __name__ == "__main__":
    test = PDF_TO_CSV()
    test.Read_filename("syllabi")
    test.data_frame()