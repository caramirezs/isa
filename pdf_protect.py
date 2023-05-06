from PyPDF2 import PdfReader, PdfWriter

pdf_path_1 = 'static/regalo.pdf'  # Ruta del archivo 1 PDF a adjuntar
pdf_output_path_1 = 'static/regalo_pss.pdf'  # Ruta del archivo PDF protegido con contraseña
password_1 = 'slytherin'

# Proteger el archivo PDF con contraseña
with open(pdf_path_1, 'rb') as input_file, open(pdf_output_path_1, 'wb') as output_file:
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(password_1)
    pdf_writer.write(output_file)