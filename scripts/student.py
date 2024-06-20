from datetime import datetime
from database import Database


class Student:
    def __init__(self, student_id, student_name, student_password, student_batch):
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_batch = student_batch

    def view_books(self):
        db = Database()
        db.view_books()

    def borrow_book(self):
        db = Database()
        selected_book_id = db.view_and_select_books()
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             No Book Selected           |')
            print('\t\t\t\t------------------------------------------')
            return

        status = db.borrow_book(self, selected_book_id)

        if status:
            trans_id, today_date, book_obj = status
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t|        Borrow Date  : {today_date}       |')
            print('\t\t\t\t------------------------------------------')
            print(book_obj)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|              Borrowed By               |')
            print('\t\t\t\t------------------------------------------')
            print(self)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|         Transaction Successful         |')
            print('\t\t\t\t------------------------------------------')
        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|    Error  :  Book is not available     |')
            print('\t\t\t\t------------------------------------------')