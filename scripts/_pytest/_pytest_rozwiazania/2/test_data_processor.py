import pytest
import time
import random
from data_processor import DataProcessor


@pytest.fixture
def processor():
    """Create fresh processor instance for each test"""
    return DataProcessor("test_dataset")


def test_initialization(processor):
    """Test processor initialization with dataset name and empty values"""
    assert processor.dataset_name == "test_dataset"
    assert processor.values == []


def test_add_valid_value(processor):
    """Test adding valid numeric value to dataset"""
    result = processor.add_value(15.5)
    assert result is True
    assert 15.5 in processor.values


def test_add_invalid_type(processor):
    """Test adding non-numeric value raises TypeError"""
    with pytest.raises(TypeError, match="Value must be a number"):
        processor.add_value("not_number")


def test_add_negative_value(processor):
    """Test adding negative value raises ValueError"""
    with pytest.raises(ValueError, match="Value must be positive"):
        processor.add_value(-5)


def test_calculate_average_valid(processor):
    """Test calculating average of stored values"""
    processor.values = [10, 20, 30]
    average = processor.calculate_average()
    assert average == 20.0


def test_calculate_average_float_precision(processor):
    """Test float precision handling in average calculation"""
    processor.values = [0.1, 0.2, 0.3]
    average = processor.calculate_average()
    assert average == pytest.approx(0.2, abs=1e-1)


def test_calculate_average_empty(processor):
    """Test calculating average on empty dataset raises error"""
    with pytest.raises(ValueError, match="No values to calculate"):
        processor.calculate_average()


def test_get_sample_data_deterministic(processor):
    """Test deterministic sample data generation with fixed seed"""
    random.seed(42)
    sample = processor.get_sample_data(3)
    assert sample == [10, 1, 0]


def test_get_statistics_with_data(processor):
    """Test statistics format with data"""
    processor.values = [5, 10, 15]
    stats = processor.get_statistics()
    
    expected = {
        "count": 3,
        "min": 5,
        "max": 15,
        "avg": 10.0
    }
    assert stats == expected


def test_get_statistics_empty(processor):
    """Test statistics for empty dataset"""
    stats = processor.get_statistics()
    expected = {"count": 0, "min": None, "max": None, "avg": None}
    assert stats == expected


def test_validate_dataset_name_valid():
    """Test valid dataset name validation"""
    valid_processor = DataProcessor("dataset_123")
    result = valid_processor.validate_dataset_name()
    assert result is True


def test_validate_dataset_name_invalid():
    """Test invalid dataset name validation"""
    invalid_processor = DataProcessor("data@set!")
    with pytest.raises(ValueError, match="Invalid dataset name"):
        invalid_processor.validate_dataset_name()


def test_get_creation_time_format(processor):
    """Test creation timestamp is float"""
    creation_time = processor.get_creation_time()
    assert isinstance(creation_time, float)


def test_get_creation_time_recent(processor):
    """Test creation time is recent"""
    now = time.time()
    creation_time = processor.get_creation_time()
    assert abs(creation_time - now) < 1.0


def test_reset_functionality(processor):
    """Test reset clears values"""
    processor.add_value(10)
    processor.add_value(20)
    processor.reset()
    assert processor.values == []