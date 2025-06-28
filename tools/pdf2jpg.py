from pdf2image import convert_from_path

def convert_pdf_to_jpg(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    output_files = []
    for i, img in enumerate(images):
        output_path = f"{output_folder}/page_{i+1}.jpg"
        img.save(output_path, 'JPEG')
        output_files.append(output_path)
    return output_files
