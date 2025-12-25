class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания; {self.year}"


if __name__ == "__main__":
    book1 = Book("Преступление и наказание", "Федор Достоевский", 1866)

    info = book1.get_info()
    print(info)

    book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    print(book2.get_info())