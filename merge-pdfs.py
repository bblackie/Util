from pypdf import PdfMerger

pdfs = ['A.pdf', 'Q2C.pdf', 'B.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append("merge/" + pdf)

merger.write("merge/result.pdf")
merger.close()