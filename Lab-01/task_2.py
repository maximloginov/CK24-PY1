char_byte = 4    # Для хранения кода одного символа нужно 4 байта.
line_char = 25   # Количество символов в строке
page_line = 50   # Число строк на странице
book_page = 100  # Количество страниц в книге
disk_byte = int(1.44 * 1024 * 1024)  # Информационный объем дискеты

book_byte = book_page * page_line * line_char * char_byte

print("Количество книг, помещающихся на дискету:", disk_byte // book_byte)
