import PyPDF2

template = PyPDF2.PdfFileReader(open('Files/super.pdf', mode='rb'))
watermark = PyPDF2.PdfFileReader(open('Files/wtr.pdf', mode='rb'))
output= PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('NewFiles/watermarked.pdf', mode='wb') as file:
        output.write(file)

