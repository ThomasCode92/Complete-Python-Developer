import PyPDF2

with open('./Files/dummy.pdf', mode='rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer.addPage(page)

    with open('./NewFiles/rotated.pdf', mode='wb') as new_file:
        writer.write(new_file)
