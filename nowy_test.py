import os
import fitz  # PyMuPDF

def find_pdf_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                return os.path.join(root, file)
    return None

def capture_areas_from_pdf(pdf_path, output_folder, areas):
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

        for area_index, area in enumerate(areas):
            left, top, width, height = area

            # Uzyskaj fragment strony jako obraz
            clip_rect = fitz.Rect(left, top, left + width, top + height)
            img = page.get_pixmap(clip=clip_rect)

            # Zapisz obraz w folderze wynikowym
            img.save(os.path.join(output_folder, f"page_{page_num + 1}_area_{area_index + 1}.png"))
            print(f"Zapisano zrzut ekranu obszaru {area_index + 1} z strony {page_num + 1}.")

    pdf_document.close()

if __name__ == "__main__":
    pdf_directory = r"C:\Users\dzemo\Desktop\Python\konwerter pit\nowawertsja\Plik_pdf"
    output_folder = r"C:\Users\dzemo\Desktop\Python\konwerter pit\nowawertsja\screenshots"

    pdf_path = find_pdf_file(pdf_directory)

    if pdf_path:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Definiuj obszary do zrzutu ekranu: (left, top, width, height)
        # Możesz dostosować te wartości w zależności od swoich potrzeb.
        areas_to_capture = [(100, 100, 200, 200), (300, 300, 150, 150)]

        capture_areas_from_pdf(pdf_path, output_folder, areas_to_capture)
        print("Zrzuty ekranu zostały pomyślnie zapisane w folderze 'screenshots'.")
    else:
        print("Nie znaleziono pliku PDF w podanym folderze.")
