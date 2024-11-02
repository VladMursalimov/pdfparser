from docx import Document

def parseDocx(doc_path):
    # Открываем файл DOCX
    document = Document(doc_path)

    # Собираем текст из всех параграфов
    text_only = "\n".join(paragraph.text.strip() for paragraph in document.paragraphs if paragraph.text.strip())

    txt_filename = doc_path.replace(".docx", ".txt")  # Название выходного файла
    with open(txt_filename, mode='w', encoding='utf-8') as txt_file:
        txt_file.write(text_only)  # Записываем текст в файл
