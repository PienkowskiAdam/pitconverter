import os
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path

def find_pdf_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                return os.path.join(root, file)
    return None

def extract_images_from_pdf(pdf_path, output_folder):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)
            for i, image in enumerate(images):
                image.save(os.path.join(output_folder, f"page_{page_num + 1}_image_{i + 1}.png"), "PNG")

if __name__ == "__main__":
    pdf_directory = r"C:\Users\dzemo\Desktop\Python\konwerter pit"
    output_folder = r"C:\Users\dzemo\Desktop\Python\cropped_images"

    pdf_path = find_pdf_file(pdf_directory)

    if pdf_path:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        extract_images_from_pdf(pdf_path, output_folder)
        print("Zdjęcia zostały pomyślnie wycięte i zapisane w folderze 'cropped_images'.")
    else:
        print("Nie znaleziono pliku PDF w podanym folderze.")
