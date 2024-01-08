import os
import fitz  # PyMuPDF

def find_pdf_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                return os.path.join(root, file)
    return None

def extract_images_from_pdf(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)
        
        for img_index, img_info in enumerate(image_list):
            img_index += 1
            img = page.get_pixmap(img_info[0])
            img.save(os.path.join(output_folder, f"page_{page_num + 1}_image_{img_index}.png"))

    pdf_document.close()

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
