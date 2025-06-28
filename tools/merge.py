from PyPDF2 import PdfMerger

def merge_pdfs(paths, output):
    merger = PdfMerger()
    for pdf in paths:
        merger.append(pdf)
    merger.write(output)
    merger.close()
