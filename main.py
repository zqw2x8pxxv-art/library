books = [
    {"title": "Война и мир", "author": "Толстой", "count": 5},
    {"title": "Преступление и наказание", "author": "Достоевский", "count": 3}
]
readers = {}

def return_book():
    print("=== Вернуть книгу ===")
    title = input("Название: ")
    print(f"Книга '{title}' возвращена в библиотеку")

def reader_books():
    print("=== Книги у читателя ===")
    reader = input("Имя читателя: ")
    if reader in readers:
        print(readers[reader])
    else:
        print(f"У читателя {reader} нет книг")

def search_by_author():
    print("=== Поиск по автору ===")
    author = input("Автор: ")
    found = False
    for b in books:
        if author.lower() in b['author'].lower():
            print(f"{b['title']} - {b['author']}")
            found = True
    if not found:
        print("Не найдено")

def most_read():
    print("=== Топ читаемых ===")
    sorted_books = sorted(books, key=lambda x: x['count'], reverse=True)
    for b in sorted_books:
        print(f"{b['title']} - выдавалась {b['count']} раз")

def main():
    while True:
        print("\n--- БИБЛИОТЕКА ---")
        print("1. Книгу вернуть")
        print("2. Книги у читателя")
        print("3. Поиск по автору")
        print("4. Самые читаемые")
        print("0. Выход")
        c = input("Выбор: ")
        if c == "1": return_book()
        elif c == "2": reader_books()
        elif c == "3": search_by_author()
        elif c == "4": most_read()
        elif c == "0": break

if __name__ == "__main__":
    main()
