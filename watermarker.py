import PyPDF2

reader1 = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()
#loop through all page
for page in range(reader1.numPages):
    reader2 = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    watermark = reader2.getPage(0) #get watermark
    page_watermark = reader1.getPage(page)
    page_watermark.mergePage(watermark) #merge page with watermark
    writer.addPage(page_watermark)
    with open(r'watermarked.pdf', 'wb') as new_file:
        writer.write(new_file)