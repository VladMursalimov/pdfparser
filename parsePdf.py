import pdfplumber
import csv
import os
import glob

import parseDoc
import pdfToDoc


def parsePdfFolder(pdf_folder):
    # Папка с PDF файлами

    # Получаем список всех PDF файлов в папке
    pdf_files = glob.glob(os.path.join(pdf_folder, "*.pdf"))

    # Проходим по каждому PDF файлу
    for pdf_path in pdf_files:
        # Имя папки для хранения CSV файлов, создаем на основе имени PDF

        output_dir = pdf_path.replace("data_pdf\\", "").replace(".pdf", "") + "_dir"
        os.makedirs(output_dir, exist_ok=True)  # Создаем папку, если она не существует

        docx_path = pdfToDoc.pdfToDocx(output_dir, pdf_path)
        parseDoc.parseDocx(docx_path)

        # Открываем PDF и создаем CSV файлы в папке
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                # Извлекаем таблицы с текущей страницы
                tables = page.extract_tables()
                for table_index, table in enumerate(tables, start=1):
                    # Имя CSV файла для каждой таблицы
                    csv_filename = f"table_page_{page_number}_table_{table_index}.csv"
                    csv_filepath = os.path.join(output_dir, csv_filename)  # Полный путь к CSV файлу

                    # Открываем CSV файл для записи
                    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as csv_file:
                        writer = csv.writer(csv_file)

                        # Проходим по каждой строке таблицы
                        for row in table:
                            # Заменяем переносы строк на пробелы и обрабатываем None
                            cleaned_list = [item.replace('\n', ' ') if item is not None else '' for item in row]
                            writer.writerow(cleaned_list)  # Записываем строку в CSV файл

                    print(
                        f"Таблица {table_index} на странице {page_number} из файла {pdf_path} сохранена в {csv_filepath}\n")
