from src.database import Database


class Service:
    def __init__(self):
        self.db = Database()

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
