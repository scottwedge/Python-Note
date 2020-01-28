fp = open(u"C:\\Users\\Jerry\\Documents\\GitHub\\Python-Note\\my script\\useful_script\\syllabi\\SPRING-2019-Biology-101-Syllabus_schedule.pdf", 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
rsrcmgr = PDFResourceManager(caching=False)
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

email_list = []
Phone_list = []
name_list = []
replace = re.compile(r'\s+')
email_mod = re.compile(r'(\w+(\.\w+)*@\w+(\.\w+)*)')
Phone_mod = re.compile(r'(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})')
name_regax = re.compile(r'(Professor:\s+|Instructor:\s+)(\w+.*)')
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # 接受该页面的LTPage对象
    layout = device.get_result()
    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
    for x in layout:
        #如果x是水平文本对象的话
        if(isinstance(x, LTTextBoxHorizontal)):
            text = re.sub(replace, ' ', x.get_text())
            text = text.strip('\n')
            if len(text) != 0:
                print(text)
email_list
Phone_list
name_list

for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # 接受该页面的LTPage对象
    layout = device.get_result()
    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
    for x in layout:
        #如果x是水平文本对象的话
        if(isinstance(x, LTTextBoxHorizontal)):
            text = re.sub(replace, ' ', x.get_text())
            print(text)

teacher = str(' Professor: Dr. Kelly Hogan ')
phone = str('Office phone: 843-6047,')


email_mod = re.compile(r'(\w+(\.\w+)*@\w+(\.\w+)*)')
phone_mod = re.compile(r'((\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}))')
name_regax = re.compile(r'(Professor:\s+|Instructor:\s+)(\w+.*)')
Phone_mod.search(phone).group(1)
