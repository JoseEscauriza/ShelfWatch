import unittest
from unittest.mock import patch, Mock
from src.service import Service


class TestServiceDq(unittest.TestCase):

    @patch('src.service.Database')
    def test_dq_display_completed_books_success(self, mock_database):
        sample_result = [
            ('test book 1', 'first_user', 'complete'),
            ('test book 2', 'second_user', 'pending')]

        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = sample_result

        mock_database.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        service = Service()

        result = service.dq_display_pending_books()
        self.assertEqual(result, [
            ('test book 1', 'first_user', 'complete'),
            ('test book 2', 'second_user', 'pending')])
