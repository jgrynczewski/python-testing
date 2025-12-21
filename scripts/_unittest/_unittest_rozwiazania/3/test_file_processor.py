import unittest
from unittest.mock import Mock
from file_processor import FileProcessor


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        """Create mock file handler and processor instance."""
        self.mock_handler = Mock()
        self.processor = FileProcessor(self.mock_handler)

    def test_process_text_converts_to_uppercase(self):
        """Test that process_text converts content to uppercase."""
        self.mock_handler.read.return_value = "hello world"
        
        result = self.processor.process_text("test.txt")
        
        self.assertEqual(result, "HELLO WORLD")

    def test_process_text_calls_read_with_filename(self):
        """Test that process_text calls read() with correct filename."""
        self.mock_handler.read.return_value = "content"
        
        self.processor.process_text("test.txt")
        
        self.mock_handler.read.assert_called_with("test.txt")

    def test_save_data_returns_handler_result(self):
        """Test that save_data returns what handler.write() returns."""
        self.mock_handler.write.return_value = True
        
        result = self.processor.save_data("output.txt", "data")
        
        self.assertTrue(result)

    def test_save_data_calls_write_with_correct_args(self):
        """Test that save_data calls write() with filename and data."""
        self.processor.save_data("output.txt", "test data")
        
        self.mock_handler.write.assert_called_with("output.txt", "test data")

    def test_copy_file_reads_and_writes(self):
        """Test that copy_file reads source and writes to destination."""
        self.mock_handler.read.return_value = "content"
        self.mock_handler.write.return_value = True
        
        result = self.processor.copy_file("source.txt", "dest.txt")
        
        self.mock_handler.read.assert_called_with("source.txt")
        self.mock_handler.write.assert_called_with("dest.txt", "content")
        self.assertTrue(result)

    def test_safe_read_returns_content_when_file_exists(self):
        """Test safe_read returns content when no exception."""
        self.mock_handler.read.return_value = "file content"
        
        result = self.processor.safe_read("existing.txt")
        
        self.assertEqual(result, "file content")

    def test_safe_read_returns_none_on_file_not_found(self):
        """Test safe_read returns None when FileNotFoundError raised."""
        self.mock_handler.read.side_effect = FileNotFoundError("File not found")
        
        result = self.processor.safe_read("missing.txt")
        
        self.assertIsNone(result)

    def test_get_file_info_when_file_exists(self):
        """Test get_file_info when file exists."""
        self.mock_handler.exists.return_value = True
        self.mock_handler.get_size.return_value = 100
        
        result = self.processor.get_file_info("test.txt")
        
        expected = {"exists": True, "size": 100}
        self.assertEqual(result, expected)

    def test_get_file_info_when_file_not_exists(self):
        """Test get_file_info when file doesn't exist."""
        self.mock_handler.exists.return_value = False
        
        result = self.processor.get_file_info("missing.txt")
        
        expected = {"exists": False, "size": 0}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()