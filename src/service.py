from src.database import Database
from src.custom_types import AuthorRow, StatusRow, state, BookRow
from typing import Optional, Tuple, TypedDict, Union
from datetime import date


class Service:
    def __init__(self):
        self.db = Database()

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

    def dq_display_reading_books(self):

        query = """
            SELECT b.title, m.username, s.status
            FROM book as b
            JOIN status as s ON b.id = s.book_id
            JOIN member as m ON m.id = s.member_id
            WHERE s.status = 'reading';
        """

        with self.db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
