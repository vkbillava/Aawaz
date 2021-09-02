import PyPDF2

def pdf_convert(file):

    pdfFileObj = open(file, 'rb')

    Reader = PyPDF2.PdfFileReader(pdfFileObj)

    pages = Reader.numPages

    print("Number of pages: ", pages)

    text = ''

    for i in range(pages):

        pageObj = Reader.getPage(i)

        text += pageObj.extractText()

    return text

    pdfFileObj.close()
