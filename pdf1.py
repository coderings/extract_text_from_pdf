#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open('1.pdf', 'rb'))
if inputpdf.isEncrypted:
    inputpdf.decrypt("")

#inputpdf = PdfFileReader(open("1.pdf", "rb"))
#inputpdf.numPages-1
output = PdfFileWriter()
output.addPage(inputpdf.getPage(5))
output.addPage(inputpdf.getPage(6))
output.addPage(inputpdf.getPage(7))
with open("hello.pdf", "wb") as outputStream:
    output.write(outputStream)

#~ from PyPDF2 import PdfFileWriter, PdfFileReader
#~ import  PyPDF2
#~ import re
#~ import string
#~ placeholder=""

#~ pdfReader = PdfFileReader(open("2.pdf", 'rb'))
#~ if pdfReader.isEncrypted:
    #~ pdfReader.decrypt("")
    #~ output = PdfFileWriter()
    #~ output.addPage(pdfReader.getPage(0))
    #~ output.addPage(pdfReader.getPage(1))
    #~ with open("lala.pdf", "wb") as outfp:
        #~ output.write(outfp)
    
    

#~ p=re.compile('.*CHAPTER\s\d{1,2}.*')
#~ locations = []

#~ def makePdf( title, beg, end):
    #~ output = PdfFileWriter()
    #~ print ("beg: ", beg)
    #~ print ("end: ", end)
    #~ title=title.strip()
    #~ print (title)
    #~ for i in range(beg, end-1): 
        #~ output.addPage(pdfReader.getPage(i))
        #~ print (i)
    
    #~ with open(title+".pdf", "wb") as outfp:
        #~ output.write(outfp)
    #~ output=None

#~ number = pdfReader.numPages
#~ for i in range( 31, number):
    #~ pageObj = pdfReader.getPage(i)
    #~ placeholder += pageObj.extractText()
    #~ lines = placeholder.split('\n')
    #~ for line in lines:
        #~ m = p.match(line)
        #~ if m!=None:
            #~ chapterTitle=lines[ len(lines)-2] 
            #~ locations.append([chapterTitle, i])

    #~ placeholder=""
#~ for i in range(0, len(locations)-1):
    #~ title=locations[i][0]
    #~ beg=locations[i][1]
    #~ try:
        #~ end=locations[i+1][1]
    #~ except:
        #~ end=507
    #~ makePdf( title, beg, end)
