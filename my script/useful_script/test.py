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

pdfFileobj = open('.\syllabi/13205.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
print(ldfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())


