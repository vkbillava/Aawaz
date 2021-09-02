from docx2python import docx2python

def doc_convert(file):

    doc = docx2python(file).text

    return doc
