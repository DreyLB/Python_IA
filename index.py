from PyPDF2 import PdfReader
import camelot
from tabula import read_pdf
import aspose.pdf as pdf
import pdfminer.high_level
#import pandas_pdf as pd


def pagesWithTable(document):
    document = PdfReader(document)
    numPage = len(document.pages)

    cont = 0
    pages = list()
    while cont < numPage:
        page = document.pages[cont]
        text = page.extract_text()
        lower = text.lower()

        # Verificando se as palavras chaves estão na pagina
        if ('qtde' in lower or 'quantidade' in lower) and ('pr. total' in lower or 'valor total' in lower) and 'item' in lower:
            pages.append(cont)

        cont += 1

    return pages


documento = pdfminer.high_level.extract_text('ata2.pdf')
print(documento)


