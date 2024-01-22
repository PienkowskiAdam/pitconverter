import pandas as pd
import re
from bs4 import BeautifulSoup

# Wczytaj zawartość pliku HTML
with open('nazwa_pliku.htm', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Utwórz obiekt BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Znajdź wszystkie bloki <nobr> w dokumencie
nobr_blocks = soup.find_all('nobr')

# Inicjalizacja pustej listy na teksty
teksty = []

# Iteracja przez wszystkie bloki <nobr>
for nobr_block in nobr_blocks:
    # Pobierz tekst z bloku <nobr>
    text_content = nobr_block.get_text(strip=True)

    # Użyj wyrażenia regularnego do podziału tekstu, obsługując więcej niż jedną spację jako separator
    teksty_blocka = re.split(r'\s{2,}', text_content)

    # Usuń puste elementy
    teksty_blocka = [tekst.strip() for tekst in teksty_blocka if tekst]

    # Dodaj teksty do ogólnej listy
    teksty.append(teksty_blocka)

# Utwórz obiekt DataFrame
result_df = pd.DataFrame(teksty)

# Zapisz do pliku Excel
result_df.to_excel('nazwa_pliku_excel.xlsx', index=False, header=False)
