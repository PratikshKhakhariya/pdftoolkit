from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from tools import merge, split, compress, pdf2jpg, jpg2pdf, pdf2docx

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Folders for file handling
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 🏠 Home route with tool list
@app.route('/')
def index():
    tools = [
        {"name": "Merge PDF", "link": "/merge", "icon": "merge.png"},
        {"name": "Split PDF", "link": "/split", "icon": "split.png"},
        {"name": "Compress PDF", "link": "/compress", "icon": "compress.png"},
        {"name": "PDF to JPG", "link": "/pdf2jpg", "icon": "pdf2jpg.png"},
        {"name": "JPG to PDF", "link": "/jpg2pdf", "icon": "jpg2pdf.png"},
        {"name": "Word to PDF", "link": "/docx2pdf", "icon": "word2pdf.png"},
        {"name": "PDF to Word", "link": "/pdf2docx", "icon": "pdf2word.png"},
    ]
    return render_template('index.html', tools=tools)

# 🔧 Merge PDF
@app.route('/merge', methods=['GET', 'POST'])
def merge_tool():
    if request.method == 'POST':
        files = request.files.getlist('pdfs')
        paths = []
        for file in files:
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            paths.append(path)

        output_path = os.path.join(OUTPUT_FOLDER, 'merged.pdf')
        merge.merge_pdfs(paths, output_path)
        return send_file(output_path, as_attachment=True)

    return render_template('merge.html')

# 🔧 Split PDF
@app.route('/split', methods=['GET', 'POST'])
def split_tool():
    if request.method == 'POST':
        file = request.files['pdf']
        start = int(request.form['start'])
        end = int(request.form['end'])

        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        output_path = os.path.join(OUTPUT_FOLDER, f'split_{filename}')
        split.split_pdf(path, output_path, start, end)
        return send_file(output_path, as_attachment=True)

    return render_template('split.html')

# 🔧 Compress PDF
@app.route('/compress', methods=['GET', 'POST'])
def compress_tool():
    if request.method == 'POST':
        file = request.files['pdf']
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        output_path = os.path.join(OUTPUT_FOLDER, f'compressed_{filename}')
        compress.compress_pdf(path, output_path)
        return send_file(output_path, as_attachment=True)

    return render_template('compress.html')

# 🔧 PDF to JPG
@app.route('/pdf2jpg', methods=['GET', 'POST'])
def pdf2jpg_tool():
    if request.method == 'POST':
        file = request.files['pdf']
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        output_folder = os.path.join(OUTPUT_FOLDER, f'jpgs_{filename}')
        os.makedirs(output_folder, exist_ok=True)

        output_paths = pdf2jpg.convert_pdf_to_jpg(path, output_folder)
        # Zip output images
        zip_path = output_folder + ".zip"
        compress.zip_folder(output_folder, zip_path)

        return send_file(zip_path, as_attachment=True)

    return render_template('pdf2jpg.html')

# 🔧 JPG to PDF
@app.route('/jpg2pdf', methods=['GET', 'POST'])
def jpg2pdf_tool():
    if request.method == 'POST':
        files = request.files.getlist('images')
        paths = []

        for file in files:
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            paths.append(path)

        output_path = os.path.join(OUTPUT_FOLDER, 'converted.pdf')
        jpg2pdf.convert_jpg_to_pdf(paths, output_path)

        return send_file(output_path, as_attachment=True)

    return render_template('jpg2pdf.html')

# 🔧 Word to PDF
@app.route('/docx2pdf', methods=['GET', 'POST'])
def docx2pdf_tool():
    if request.method == 'POST':
        file = request.files['docx']
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        output_path = os.path.join(OUTPUT_FOLDER, f'{filename}.pdf')
        docx2pdf.convert_docx_to_pdf(path, output_path)
        return send_file(output_path, as_attachment=True)

    return render_template('docx2pdf.html')

# 🔧 PDF to Word
@app.route('/pdf2docx', methods=['GET', 'POST'])
def pdf2docx_tool():
    if request.method == 'POST':
        file = request.files['pdf']
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        output_path = os.path.join(OUTPUT_FOLDER, f'{filename}.docx')
        pdf2docx.convert_pdf_to_docx(path, output_path)
        return send_file(output_path, as_attachment=True)

    return render_template('pdf2docx.html')

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)
