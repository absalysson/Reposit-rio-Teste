#Sistema de Impressão Cambio


import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PageRange


pdfFileObj = open ('Z:\Importacao\TRADINGS - TOUQUET E LICKY\GERENCIAL\REPORTS FP&A\Fechamento de Cambio\CAMBIO MARÇO.pdf', 'rb')
print(pdfFileObj)
pdfReader = PyPDF2.PdfFileReader (pdfFileObj)
imprimir = (pdfReader.numPages)
print(imprimir)
pageObj = pdfReader.getPage(1)
trazer = "valores"

# extrai texto do objeto
##imprimir2 = (pageObj.extractText())
##print(imprimir2)


#salvamento
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)
newFileName = 'COTAÇÃO ITAU.pdf'
newFile = open ('Z:\Importacao\TRADINGS - TOUQUET E LICKY\GERENCIAL\REPORTS FP&A\Fechamento de Cambio'+newFileName,'wb')
pdfWriter.write (newFile)
pdfFileObj.close()
newFile.close()