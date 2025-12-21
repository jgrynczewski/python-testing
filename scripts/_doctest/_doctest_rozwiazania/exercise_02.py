import random
import time


class DataProcessor:
    """Process and analyze numerical data with validation.
    
    Module-level example:
    >>> processor = DataProcessor("dataset1") 
    >>> processor.add_value(10.5)
    True
    """
    
    def __init__(self, dataset_name):
        """Initialize processor with dataset name.
        
        Test initialization:
        >>> processor = DataProcessor("test")
        >>> processor.dataset_name
        'test'
        >>> processor.values
        []
        """
        self.dataset_name = dataset_name
        self.values = []
        self.created_at = time.time()
    
    def add_value(self, value):
        """Add numeric value to dataset.
        
        Valid number:
        >>> processor = DataProcessor("test")
        >>> processor.add_value(15.5)
        True
        >>> processor.values
        [15.5]
        
        Invalid type (should raise TypeError with message "Value must be a number"):
        >>> processor.add_value("not_number")
        Traceback (most recent call last):
            ...
        TypeError: Value must be a number
        
        Negative value (should raise ValueError with message "Value must be positive"):
        >>> processor.add_value(-5)
        Traceback (most recent call last):
            ...
        ValueError: Value must be positive
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Value must be positive")
        self.values.append(value)
        return True
    
    def calculate_average(self):
        """Calculate average of stored values.
        
        Valid calculation:
        >>> processor = DataProcessor("test")
        >>> processor.values = [10, 20, 30]
        >>> processor.calculate_average()
        20.0
        
        Float precision (handle 0.1 + 0.2 + 0.3 properly):
        >>> processor = DataProcessor("test")
        >>> processor.values = [0.1, 0.2, 0.3]
        >>> round(processor.calculate_average(), 1)
        0.2
        
        Empty dataset (should raise ValueError with message "No values to calculate"):
        >>> processor = DataProcessor("test")
        >>> processor.calculate_average()
        Traceback (most recent call last):
            ...
        ValueError: No values to calculate
        """
        if not self.values:
            raise ValueError("No values to calculate")
        return sum(self.values) / len(self.values)
    
    def get_sample_data(self, size=3):
        """Generate sample data for testing.
        
        Deterministic sample (set random.seed(42) for consistent results):
        >>> random.seed(42)
        >>> processor = DataProcessor("test")
        >>> processor.get_sample_data(3)
        [10, 1, 0]
        """
        return [random.randint(0, 10) for _ in range(size)]
    
    def get_statistics(self):
        """Return dataset statistics as dict.
        
        Statistics format:
        >>> processor = DataProcessor("test")
        >>> processor.values = [5, 10, 15]
        >>> stats = processor.get_statistics()
        >>> stats['count']
        3
        >>> stats['min']
        5
        >>> stats['max']
        15
        >>> stats['avg']
        10.0
        
        Empty dataset statistics:
        >>> processor = DataProcessor("test")
        >>> processor.get_statistics()
        {'count': 0, 'min': None, 'max': None, 'avg': None}
        """
        if not self.values:
            return {"count": 0, "min": None, "max": None, "avg": None}
        
        return {
            "count": len(self.values),
            "min": min(self.values),
            "max": max(self.values), 
            "avg": self.calculate_average()
        }
    
    def validate_dataset_name(self):
        """Validate dataset name format.
        
        Valid name pattern (alphanumeric + underscore):
        >>> processor = DataProcessor("dataset_123")
        >>> processor.validate_dataset_name()
        True
        
        Invalid characters (should raise ValueError with message "Invalid dataset name"):
        >>> processor = DataProcessor("data@set!")
        >>> processor.validate_dataset_name()
        Traceback (most recent call last):
            ...
        ValueError: Invalid dataset name
        """
        import re
        if not re.match(r'^[a-zA-Z0-9_]+$', self.dataset_name):
            raise ValueError("Invalid dataset name")
        return True
    
    def get_creation_time(self):
        """Return creation timestamp.
        
        Timestamp format:
        >>> processor = DataProcessor("test")
        >>> isinstance(processor.get_creation_time(), float)
        True

        Kilka propozycji na testowanie czasu

        1. Testuj że jest "świeży" (niedawny):
        >>> import time
        >>> now = time.time()
        >>> processor = DataProcessor("test")
        >>> abs(processor.get_creation_time() - now) < 1.0  # w ciągu sekundy
        True

        3. Testuj że jest większy niż znana data:
        >>> processor.get_creation_time() > 1600000000  # > 2020 rok
        True

        4. Porównaj dwie instancje:
        >>> p1 = DataProcessor("test1")
        >>> time.sleep(0.01)
        >>> p2 = DataProcessor("test2")
        >>> p2.get_creation_time() > p1.get_creation_time()
        True

        5. Mock time (najbardziej kontrolowane):  - ALE NAJLEPIEJ UNIKAĆ MOCKOWANIA W DOCKTESTACH, bo testy nie są
        separowane i mock będzie dotyczył wszystkich testów w danej sesji.
        >>> import time
        >>> fixed_time = 1234567890.0
        >>> old_time = time.time
        >>> time.time = lambda: fixed_time  # mock może zepsuć inne testy
        >>> processor = DataProcessor("test")
        >>> processor.get_creation_time()
        1234567890.0
        >>> time.time = old_time  # restore
        """
        return self.created_at
    
    def reset(self):
        """Clear all values and reset processor.
        
        Reset functionality:
        >>> processor = DataProcessor("test")
        >>> processor.add_value(10)
        True
        >>> processor.add_value(20)
        True
        >>> processor.reset()
        True
        >>> processor.values
        []
        """
        self.values = []
        return True
