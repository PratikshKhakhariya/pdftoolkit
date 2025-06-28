from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_path, start, end):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for i in range(start - 1, end):
        writer.add_page(reader.pages[i])
    with open(output_path, 'wb') as f:
        writer.write(f)
