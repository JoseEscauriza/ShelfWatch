from psycopg import Connection
from src.database import Database
from src.custom_types import AuthorRow, StatusRow, BookRow
from typing import Union


class Service:
    def __init__(self):
        self.db: Connection = Database()  # noqa

    def dq_display_pending_books(self):

        query = """
            SELECT b.title, m.username, s.status
            FROM book as b
            JOIN status as s ON b.id = s.book_id
            JOIN member as m ON m.id = s.member_id
            WHERE s.status = 'pending';
        """

        with self.db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def dq_display_completed_books(self):

        query = """
            SELECT b.title, m.username, s.status
            FROM book as b
            JOIN status as s ON b.id = s.book_id
            JOIN member as m ON m.id = s.member_id
            WHERE s.status = 'complete';
        """

        with self.db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def dq_display_book_by_author(self, author_name: str):
        query = """
            SELECT b.title, a.author_first_name || ' ' || a.author_last_name AS author 
            FROM book AS b
            JOIN author AS a ON b.author_id = a.id
            WHERE a.author_first_name ILIKE %s or a.author_last_name ILIKE %s;
        """

        with self.db.cursor() as cursor:
            cursor.execute(query, (f"%{author_name}%", f"%{author_name}%"))
            result = cursor.fetchall()
            return result

    def dq_display_books_by_title(self, title: str):
        query = """
                    SELECT b.title, b.description, b.genre, a.author_first_name || ' ' || a.author_last_name as author 
                    FROM book AS b
                    JOIN author AS a ON b.author_id = a.id
                    WHERE b.title ILIKE %s
                """

        with self.db.cursor() as cursor:
            cursor.execute(query, (f"%{title}%",))
            result = cursor.fetchall()
            return result

    def dm_insert_data(self, table: str, data: Union[str, AuthorRow, StatusRow, BookRow]):
        if table == 'member':
            query = """
                INSERT INTO member
                VALUES (default, %s) RETURNING id;
            """

            with self.db.cursor() as cursor:
                cursor.execute(query, (data, ))
                result = cursor.fetchone()[0]
                self.db.commit()
                return result

        if table == 'book':
            query = """
                INSERT INTO book
                VALUES (default, %s, %s, %s, %s) RETURNING id;
            """

            with self.db.cursor() as cursor:
                cursor.execute(query, tuple(data.values()))
                result = cursor.fetchone()[0]
                self.db.commit()
                return result

        if table == 'author':
            query = """
                INSERT INTO author
                VALUES (default, %s, %s, %s) RETURNING id;
            """

            with self.db.cursor() as cursor:
                cursor.execute(query, tuple(data.values()))
                result = cursor.fetchone()[0]
                self.db.commit()
                return result

    def dm_prompt_member_data(self):
        member_name = input("Please insert a username to store in the database: ")
        return member_name

    def dm_prompt_author_data(self):
        author_first_name = input("Author's first name: ")
        author_last_name = input("Author's last name: ")
        author_birthdate = input("Author's birthdate: ")

        return {
            'author_first_name': author_first_name if author_first_name else None,
            'author_last_name': author_last_name,
            'author_birthdate': author_birthdate if author_birthdate else None
        }

    def dm_prompt_book_data(self):
        author_id = input("Please insert the author's ID: ")
        title = input("Please insert the book's title: ")
        description = input("Please enter the book's short description: ")
        genre = input("Please enter the book's genre: ")

        return {
            'author_id': int(author_id) if author_id else None,
            'title': title,
            'description': description if description else None,
            'genre': genre
        }