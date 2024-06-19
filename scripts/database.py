# Importing the required libraries
import csv
import datetime
import os
from book import *

class Database:
    # Intilizing the Database Object (Null in this case)
    def __init__(self):
        pass

    # This method is used to get all the book details from the books file.
    def view_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                All Book(s)             |')
            print('\t\t\t\t------------------------------------------')
            for lines in csv_file:
                self.print_it(lines)

                if count % 4 == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|       Press enter to view more...      |')
                    print('\t\t\t\t|       Press other key to exit          |')
                    print('\t\t\t\t------------------------------------------')
                    inp = input('\t\t\t\t\t-> ')
                    if len(inp) != 0:
                        break
                count += 1

    # This method is used to view all the books and get the valid book id that the user has selected.
    def view_and_select_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                All Book(s)             |')
            print('\t\t\t\t------------------------------------------')
            for lines in csv_file:
                self.print_it(lines)

                if count % 4 == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|        Provide accurate Book ID.       |')
                    print('\t\t\t\t|        Press enter to view more...     |')
                    print('\t\t\t\t------------------------------------------')
                    inp = input('\t\t\t\t\t-> ')
                    if len(inp) != 0:
                        return inp
                count += 1

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|        Provide accurate Book ID.       |')
        print('\t\t\t\t|        Press enter to exit.            |')
        print('\t\t\t\t------------------------------------------')
        inp = input('\t\t\t\t\t-> ')

        if len(inp) == 0:
            return False

        return inp