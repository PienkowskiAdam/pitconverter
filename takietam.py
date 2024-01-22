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

# Zapisz do pliku Excel (pierwszy arkusz)
result_df.to_excel('nazwa_pliku_excel.xlsx', index=False, header=False, sheet_name='Początkowe_Dane')

# Dodaj drugi arkusz z wymaganymi kolumnami
nazwy_kolumn = [
    'Numer osobowy', 'NR_LISTY', 'Kwota', 'KOD_SKLADNIKA', 'St.dz.', 'OPIS_SKLADNIKA', 
    'Zasiłek za czas Od', 'Zasiłek za czas Do', '%', 'ILOŚĆ', 'ANAL_T0', 'ANAL_T1', 
    'ANAL_T2', 'Data wypłaty', 'ANAL_T4', 'ANAL_T5', 'ANAL_T6', 'ANAL_T7', 
    'Zasiłek za czas - Dni', 'OKRES:', 'Kod.abs.', 'Kod lit.', 'Składnik wynagrodzenia', 
    'KodZUS', 'FP/ZUS'
]

wynik_df = pd.DataFrame(columns=nazwy_kolumn)

# Zapisz do pliku Excel (drugi arkusz)
with pd.ExcelWriter('nazwa_pliku_excel.xlsx', engine='xlsxwriter') as writer:
    result_df.to_excel(writer, index=False, header=False, sheet_name='Początkowe_Dane')
    wynik_df.to_excel(writer, index=False, sheet_name='Wynik', startcol=len(result_df.columns) + 2)
