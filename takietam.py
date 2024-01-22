import pandas as pd
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

    # Podziel tekst na części, używając &nbsp; jako separatora
    teksty_blocka = [tekst.strip() for tekst in text_content.split('&nbsp;')]

    # Usuń puste elementy
    teksty_blocka = [tekst for tekst in teksty_blocka if tekst]

    # Dodaj teksty do ogólnej listy
    teksty.append(teksty_blocka)

# Utwórz obiekt DataFrame
result_df = pd.DataFrame(teksty)

# Zapisz do pliku Excel
result_df.to_excel('nazwa_pliku_excel.xlsx', index=False, header=False)
