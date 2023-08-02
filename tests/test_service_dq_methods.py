import unittest
from unittest.mock import patch, Mock
from src.service import Service


class TestServiceDq(unittest.TestCase):

    @patch('src.service.Database')
    def test_dq_display_completed_books_success(self, mock_database):
        mock_result = [
            ('test book 1', 'first_user', 'complete'),
            ('test book 2', 'second_user', 'pending')]

        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = mock_result
        mock_database.return_value.cursor.return_value.__enter__.return_value = mock_cursor
        service = Service()
        result = service.dq_display_pending_books()
        self.assertEqual(result, mock_result)

    @patch('src.service.Database')
    def test_dq_display_book_by_author_success_by_first_name(self, mock_database):
        mock_result = [
            ("test boo1", "James Ronald"),
            ("test boo2", "James Ronald"),
            ("test boo2", "James Brain")]

        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = mock_result
        mock_database.return_value.cursor.return_value.__enter__.return_value = mock_cursor
        service = Service()
        result = service.dq_display_book_by_author("James")
        self.assertEqual(result, mock_result)

    @patch('src.service.Database')
    def test_dq_display_book_by_author_success_by_second_name(self, mock_database):
        mock_result = [
            ("test boo1", "James Ronald"),
            ("test boo2", "James Ronald")]

        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = mock_result
        mock_database.return_value.cursor.return_value.__enter__.return_value = mock_cursor
        service = Service()
        result = service.dq_display_book_by_author("Ronald")
        self.assertEqual(result, mock_result)

    @patch('src.service.Database')
    def test_dq_display_books_by_title_success(self, mock_database):
        mock_result = [
            ("Norse Mythology", "test description", "test genre", "test author"),
            ("Norse Mythology volume 2", "test description", "test genre", "test author"),
            ("Valhalla test norse", "test description", "test genre", "test author"),
        ]

        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = mock_result
        mock_database.return_value.cursor.return_value.__enter__.return_value = mock_cursor
        service = Service()
        result = service.dq_display_book_by_author("norse")
        self.assertEqual(result, mock_result)
