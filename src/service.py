from psycopg import Connection
from src.database import Database


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
