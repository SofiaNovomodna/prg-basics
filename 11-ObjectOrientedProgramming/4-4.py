class Ebook:
    def __init__(self, title, author, number_of_pages):
        self.title =title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 1
        self.is_opened = False

    def go_forward(self):
        if self.is_opened == True:
            self.current_page +=1
        else:
            print('The book is closed')
    def go_backward(self):
        if self.is_opened == True:
            self.current_page -=1
        else:
            print('The book is closed')

    def open(self):
        self.is_opened = True
    def close(self):
        self.is_opened = False

    def info(self):
        print(f'title: {self.title}, author: {self.author}, page numbers: {self.number_of_pages}, current page no: {self.current_page}')


book1 = Ebook('The Book of Bill: Alex Hirsch', 'Alex Hirsch', 208)
book1.open()
book1.info()
book1.go_forward()
book1.go_forward()
book1.go_forward()
book1.go_forward()
book1.go_forward()
book1.info()
book1.close()
book1.go_forward()