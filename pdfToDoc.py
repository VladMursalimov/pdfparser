from pdf2docx import Converter
import os

def pdfToDocx(save_folder, pdf_path):
    # Указываем имя выходного DOCX файла
    docx_filename = os.path.basename(pdf_path).replace(".pdf", ".docx")
    # Создаем полный путь к выходному DOCX файлу в указанной папке
    docx_path = os.path.join(save_folder, docx_filename)

    # Создаем объект конвертера
    cv = Converter(pdf_path)
    # Конвертируем PDF в DOCX
    cv.convert(docx_path, start=0, end=None)  # start и end задают страницы для конвертации, None означает все страницы
    cv.close()

    print("Конвертация завершена! Файл сохранен по пути:", docx_path)

    return docx_path
