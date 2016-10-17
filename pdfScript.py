import PyPDF2
import re


def pdfPageFunction (pdfFile):
    pdfFileObj = open(pdfFile, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    page = pageObj.extractText()
    return page

def pdfValueFinder (pdfPage,findVal):
    valuePosition = pdfPage.find(findVal, 10)
    return valuePosition
