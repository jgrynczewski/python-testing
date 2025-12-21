import unittest
import time
import random
from data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        """Create fresh processor instance for each test"""
        self.processor = DataProcessor("test_dataset")

    def test_initialization(self):
        """Test processor initialization with dataset name and empty values"""
        self.assertEqual(self.processor.dataset_name, "test_dataset")
        self.assertEqual(self.processor.values, [])

    def test_add_valid_value(self):
        """Test adding valid numeric value to dataset"""
        result = self.processor.add_value(15.5)
        self.assertTrue(result)
        self.assertIn(15.5, self.processor.values)

    def test_add_invalid_type(self):
        """Test adding non-numeric value raises TypeError"""
        with self.assertRaisesRegex(TypeError, "Value must be a number"):
            self.processor.add_value("not_number")

    def test_add_negative_value(self):
        """Test adding negative value raises ValueError"""
        with self.assertRaisesRegex(ValueError, "Value must be positive"):
            self.processor.add_value(-5)

    def test_calculate_average_valid(self):
        """Test calculating average of stored values"""
        self.processor.values = [10, 20, 30]
        average = self.processor.calculate_average()
        self.assertEqual(average, 20.0)

    def test_calculate_average_float_precision(self):
        """Test float precision handling in average calculation"""
        self.processor.values = [0.1, 0.2, 0.3]
        average = self.processor.calculate_average()
        self.assertAlmostEqual(average, 0.2, places=1)

    def test_calculate_average_empty(self):
        """Test calculating average on empty dataset raises error"""
        with self.assertRaisesRegex(ValueError, "No values to calculate"):
            self.processor.calculate_average()

    def test_get_sample_data_deterministic(self):
        """Test deterministic sample data generation with fixed seed"""
        random.seed(42)
        sample = self.processor.get_sample_data(3)
        self.assertEqual(sample, [10, 1, 0])

    def test_get_statistics_with_data(self):
        """Test statistics format with data"""
        self.processor.values = [5, 10, 15]
        stats = self.processor.get_statistics()
        
        expected = {
            "count": 3,
            "min": 5,
            "max": 15,
            "avg": 10.0
        }
        self.assertEqual(stats, expected)

    def test_get_statistics_empty(self):
        """Test statistics for empty dataset"""
        stats = self.processor.get_statistics()
        expected = {"count": 0, "min": None, "max": None, "avg": None}
        self.assertEqual(stats, expected)

    def test_validate_dataset_name_valid(self):
        """Test valid dataset name validation"""
        valid_processor = DataProcessor("dataset_123")
        result = valid_processor.validate_dataset_name()
        self.assertTrue(result)

    def test_validate_dataset_name_invalid(self):
        """Test invalid dataset name validation"""
        invalid_processor = DataProcessor("data@set!")
        with self.assertRaisesRegex(ValueError, "Invalid dataset name"):
            invalid_processor.validate_dataset_name()

    def test_get_creation_time_format(self):
        """Test creation timestamp is float"""
        creation_time = self.processor.get_creation_time()
        self.assertIsInstance(creation_time, float)

    def test_get_creation_time_recent(self):
        """Test creation time is recent"""
        now = time.time()
        creation_time = self.processor.get_creation_time()
        self.assertLess(abs(creation_time - now), 1.0)

    def test_reset_functionality(self):
        """Test reset clears values"""
        self.processor.add_value(10)
        self.processor.add_value(20)
        self.processor.reset()
        self.assertEqual(self.processor.values, [])


if __name__ == '__main__':
    unittest.main()