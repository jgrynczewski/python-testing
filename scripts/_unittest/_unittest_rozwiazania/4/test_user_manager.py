import unittest
from unittest.mock import patch, Mock
from user_manager import UserManager


class TestUserManager(unittest.TestCase):

    def setUp(self):
        """Create UserManager instance for testing."""
        self.manager = UserManager("test.db")

    @patch('user_manager.sqlite3.connect')
    def test_create_user_returns_user_id(self, mock_connect):
        """Test that create_user returns the generated user ID."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.lastrowid = 123
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.create_user("John Doe", "john@test.com")
        
        # Assert
        self.assertEqual(result, 123)

    @patch('user_manager.sqlite3.connect')  
    def test_create_user_executes_correct_sql(self, mock_connect):
        """Test that create_user executes correct SQL with parameters."""
        # Setup mock
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        self.manager.create_user("John Doe", "john@test.com")
        
        # Assert
        mock_cursor.execute.assert_called_with(
            "INSERT INTO users (name, email) VALUES (?, ?)", 
            ("John Doe", "john@test.com")
        )

    @patch('user_manager.sqlite3.connect')
    def test_get_user_returns_user_dict(self, mock_connect):
        """Test that get_user returns user dict when user exists."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.fetchone.return_value = (1, "John Doe", "john@test.com")
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.get_user(1)
        
        # Assert
        expected = {"id": 1, "name": "John Doe", "email": "john@test.com"}
        self.assertEqual(result, expected)

    @patch('user_manager.sqlite3.connect')
    def test_get_user_returns_none_when_not_found(self, mock_connect):
        """Test that get_user returns None when user not found."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.fetchone.return_value = None
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.get_user(999)
        
        # Assert
        self.assertIsNone(result)

    @patch('user_manager.sqlite3.connect')
    def test_delete_user_returns_true_when_deleted(self, mock_connect):
        """Test that delete_user returns True when user was deleted."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.rowcount = 1
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.delete_user(1)
        
        # Assert
        self.assertTrue(result)

    @patch('user_manager.sqlite3.connect')
    def test_delete_user_returns_false_when_not_found(self, mock_connect):
        """Test that delete_user returns False when user not found."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.rowcount = 0
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.delete_user(999)
        
        # Assert
        self.assertFalse(result)

    @patch('user_manager.sqlite3.connect')
    def test_user_exists_returns_true_when_found(self, mock_connect):
        """Test that user_exists returns True when email found."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.fetchone.return_value = (1,)
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.user_exists("john@test.com")
        
        # Assert
        self.assertTrue(result)

    @patch('user_manager.sqlite3.connect')
    def test_user_exists_returns_false_when_not_found(self, mock_connect):
        """Test that user_exists returns False when email not found."""
        # Setup mock
        mock_cursor = Mock()
        mock_cursor.fetchone.return_value = (0,)
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Test
        result = self.manager.user_exists("notfound@test.com")
        
        # Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()