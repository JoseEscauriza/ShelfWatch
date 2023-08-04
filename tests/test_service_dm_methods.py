import unittest
from unittest.mock import patch, Mock
from src.service import Service

class TestServiceDm(unittest.TestCase):

    @patch('src.service.Database')
    def test_dm_insert_member(self, mock_db):
        expected_result = ('10, testuser')
        mock_cursor = Mock()
        mock_cursor.fetchone.return_value = expected_result

        mock_db.return_value.cursor.return_value.__enter__.return_value = mock_cursor
        # Vitalii how did you even know what to type here? xD

        service = Service()
        service.dm_insert_data('member', ('default', 'testuser'))
        result = mock_cursor.fetchone()
        print(result)
        self.assertEqual(result, expected_result)

        """
        Is this test even valid? We are specifying in like 11 that fetchone = expected result, 
        so of course that assertion would be true?
        """