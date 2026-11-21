from pypdf import PdfWriter

pdfs = ['A.pdf', 'Q2C.pdf', 'B.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append("merge/" + pdf)

merger.write("merge/result.pdf")
merger.close()