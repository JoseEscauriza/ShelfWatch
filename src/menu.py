import sys
from src.service import Service
from tabulate import tabulate

service = Service()


class Menu:

    @staticmethod
    def display_menu():
        while True:
            print("""
                WELCOME TO SHELFWATCH!
                
                MENU
                -----
                
                1. Data query
                2. Data manipulation
                3. Exit
                """)

            option = input("Please pick an option (1-3): ")

            match option:
                case '1':
                    Menu.display_dq_menu()
                case '2':
                    Menu.display_dm_menu()
                case '3':
                    sys.exit()
                case _:
                    print(
                        "Option not recognized, please pick a valid option (1-3)")

    @staticmethod
    def display_dq_menu():
        while True:
            print("""
                1. Display pending books
                2. Display reading books
                3. Display completed books
                4. Display books by Author
                5. Display books by Title
                6. Display reading records in a given timeframe
                7. Display 10 most popular books
                8. Display 10 least popular books
                9. Return to main menu
                10. Exit program
                """)

            option = input("Please pick an option: ")

            match option:
                case '1':
                    data = service.dq_display_pending_books()
                    table = [tab for tab in data]
                    print(tabulate(table, headers=['Title', 'Username', 'Status'], tablefmt='fancy_grid'))
                case '2':
                    data = service.dq_display_reading_books()
                    table = [tab for tab in data]
                    print(tabulate(table, headers=['Title', 'Username', 'Status'], tablefmt='fancy_grid'))

                case '3':
                    data = service.dq_display_completed_books()
                    table = [tab for tab in data]
                    print(tabulate(table, headers=['Title', 'Username', 'Status'], tablefmt='fancy_grid'))

                case '4':
                    pass

                case '5':
                    pass

                case '6':
                    pass

                case '7':
                    pass

                case '8':
                    pass

                case '9':
                    Menu.display_menu()

                case '10':
                    sys.exit()

                case _:
                    print("Option not recognized, please pick a valid option (1-3)")

    @staticmethod
    def display_dm_menu():
        while True:
            print("""
                1. Insert data
                2. Update data
                3. Delete data
                4. Return to main menu
                5. Exit program
                """)

            option = input("Please pick an option: ")

            match option:
                case '1':
                    Menu.insert_data_menu()
                    option2 = input("Please pick what you'd like to insert: ")
                    match option2:
                        case '1':
                            table = 'member'
                            data = service.dm_prompt_member_data()
                            returning_id = service.dm_insert_data(table, data)
                            print(returning_id)

                        case '2':
                            table = 'author'
                            data = service.dm_prompt_author_data()
                            returning_id = service.dm_insert_data(table, data)
                            print(returning_id)

                        case '3':
                            table = 'book'
                            data = service.dm_prompt_book_data()
                            returning_id = service.dm_insert_data(table, data)
                            print(returning_id)

                        case '4':
                            pass
                        case '5':
                            Menu.display_menu()
                        case '6':
                            sys.exit()
                        case _:
                            print("Invalid option, please try again")
                case '4':
                    break
                case '5':
                    sys.exit()
                case _:
                    print("Option not recognized, please try again")
    @staticmethod
    def insert_data_menu():
        print("""
            1. Insert Member
            2. Insert Author
            3. Insert Book
            4. Return to previous menu
            5. Return to main menu
            6. Exit program
            """)

    @staticmethod
    def update_data_menu():
        print("""
            1. Update Member
            2. Update Book
            3. Update Author
            4. Return to previous menu
            5. Return to main menu
            6. Exit program
            """)

    @staticmethod
    def delete_data_menu():
        print("""
            1. Delete Member
            2. Delete Book
            3. Delete Author
            4. Return to previous menu
            5. Return to main menu
            6. Exit program
            """)
