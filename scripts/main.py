from main_helper import *
from student import *
from librarian import *
from pwinput import pwinput
import os


def start():
    wrong_option = 5
    failed_auth = 5

    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|                  Home                  |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          1. Student Login              |')
        print('\t\t\t\t|          2. Student Register           |')
        print('\t\t\t\t|          3. Librarian Login            |')
        print('\t\t\t\t|          4. Librarian Register         |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress enter to exit')
        print('\t\t\t\t\tEnter your option')
        choice = input('\t\t\t\t\t-> ').strip()

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                if failed_auth < 0:
                    break
                print('\t\t\t\t\tEnter your ID ')
                stud_id = input('\t\t\t\t\t-> ').strip()

                print('\t\t\t\t\tEnter your Password')
                stud_pass = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                if len(stud_id) == 0 or len(stud_pass) == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|         Error : Invalid Entry!         |')
                    print(f'\t\t\t\t\t|      Remaining attempts : {failed_auth}      |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1
                    continue

                stud_obj = stud_auth(stud_id, stud_pass)

                if stud_obj:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Hello!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print(stud_obj)
                    print('\t\t\t\t------------------------------------------')

                    stud_options(stud_obj)
                else:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|    Error : Authentication Failed!      |')
                    print(f'\t\t\t\t|    Remaining attempts : {failed_auth}              |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1

            case '2':
                status = False
                while True:
                    print('\t\t\t\t\tEnter your Name')
                    stud_name = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter your Password')
                    stud_pass_1 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    print('\t\t\t\t\tRe-enter your Password')
                    stud_pass_2 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    if stud_pass_1 != stud_pass_2:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|          Password not matching         |')
                        print('\t\t\t\t|           Press enter to exit          |')
                        print('\t\t\t\t------------------------------------------')
                        ch = input('\t\t\t\t\t\t-> ')
                        break

                    print('\t\t\t\t\tEnter Batch')
                    stud_batch = input('\t\t\t\t\t-> ')

                    if len(stud_name) < 1 or len(stud_pass_1) < 1 or len(stud_pass_2) < 1 or len(stud_batch) < 1:
                        print('\t\t\t\t\tPlease enter a valid student details.')
                        ch = input('\t\t\t\t\tPress Enter to continue....')
                        if len(ch) <= 0:
                            break
                    else:
                        status = True
                        break

                if status:
                    stud = Student(student_id=create_id(),
                                   student_name=stud_name,
                                   student_password=stud_pass_1,
                                   student_batch=stud_batch)

                    save_student(stud)

            case '3':
                if failed_auth < 0:
                    break
                print('\t\t\t\t\tEnter your ID')
                lib_id = input('\t\t\t\t\t-> ').strip()

                print('\t\t\t\t\tEnter your Password')
                lib_pass = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                if len(lib_id) == 0 or len(lib_pass) == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|         Error : Invalid Entry!         |')
                    print(f'\t\t\t\t\t|      Remaining attempts : {failed_auth}      |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1
                    continue

                lib_obj = lib_auth(lib_id, lib_pass)

                if lib_obj:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Hello!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print(lib_obj)
                    print('\t\t\t\t------------------------------------------')

                    lib_options(lib_obj)
                else:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|    Error : Authentication Failed!      |')
                    print(f'\t\t\t\t|    Remaining attempts : {failed_auth}              |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1

            case '4':
                status = False
                while True:
                    print('\t\t\t\t\tEnter your Name')
                    lib_name = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter your Password')
                    lib_pass_1 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    print('\t\t\t\t\tRe-enter your Password')
                    lib_pass_2 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    if lib_pass_1 != lib_pass_2:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|          Password not matching         |')
                        print('\t\t\t\t|           Press enter to exit          |')
                        print('\t\t\t\t------------------------------------------')
                        ch = input('\t\t\t\t\t-> ')
                        break

                    if len(lib_name) < 1 or len(lib_pass_1) < 1 or len(lib_pass_2) < 1:
                        print('\t\t\t\t\tPlease enter a valid details.')
                        ch = input('\t\t\t\t\tPress Enter to continue....')
                        if len(ch) <= 0:
                            break
                    else:
                        status = True
                        break

                if status:
                    lib = Librarian(librarian_id=create_lib_id(),
                                    librarian_name=lib_name,
                                    librarian_password=lib_pass_1)

                    save_librarian(lib)

            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1