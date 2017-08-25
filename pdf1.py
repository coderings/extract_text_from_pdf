#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyPDF2 import PdfFileWriter, PdfFileReader
import  PyPDF2
import re
import string
placeholder=""

p=re.compile('.*CHAPTER\s\d{1,2}.*')
q=re.compile('.*Switch Port Configuration.*')

pdfFileObj = open('1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
number = pdfReader.numPages
#for i in range( 32,34):
pageObj = pdfReader.getPage(59)
placeholder += pageObj.extractText()
lines = placeholder.split('\n')
#~ for line in lines:
    #~ m = p.match(line)
    #~ if m!=None:
        #~ print (lines[0], lines[1], lines[2], lines[3])
        #~ print ("//////////////////////////////////////")
        #~ print (lines.index(line))
        #~ print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print (lines)
placeholder=""
    

#~ for i in range(inputpdf.numPages):
    #~ output = PdfFileWriter()
    #~ output.addPage(inputpdf.getPage(i))
    #~ with open("document-page%s.pdf" % i, "wb") as outputStream:
        #~ output.write(outputStream)


