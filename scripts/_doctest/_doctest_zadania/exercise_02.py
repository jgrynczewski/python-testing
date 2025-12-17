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
        >>> ... # Test DataProcessor("test") has dataset_name "test" and empty values list
        """
        self.dataset_name = dataset_name
        self.values = []
        self.created_at = time.time()
    
    def add_value(self, value):
        """Add numeric value to dataset.
        
        Valid number:
        >>> ... # Test processor.add_value(15.5) returns True and adds to values
        
        Invalid type (should raise TypeError with message "Value must be a number"):
        >>> ... # Test processor.add_value("not_number") raises TypeError
        
        Negative value (should raise ValueError with message "Value must be positive"):
        >>> ... # Test processor.add_value(-5) raises ValueError
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
        >>> ... # Test processor with values [10, 20, 30] returns average 20.0
        
        Float precision (handle 0.1 + 0.2 + 0.3 properly):
        >>> ... # Test processor with values [0.1, 0.2, 0.3] has average 0.2 (use proper precision handling)
        
        Empty dataset (should raise ValueError with message "No values to calculate"):
        >>> ... # Test empty processor raises ValueError on calculate_average()
        """
        if not self.values:
            raise ValueError("No values to calculate")
        return sum(self.values) / len(self.values)
    
    def get_sample_data(self, size=3):
        """Generate sample data for testing.
        
        Deterministic sample:
        >>> ... # Test with the given seed
        """
        return [random.randint(0, 10) for _ in range(size)]
    
    def get_statistics(self):
        """Return dataset statistics as dict.
        
        Statistics format:
        >>> ... # Test processor with values [5, 10, 15] returns dict with keys 'count', 'min', 'max', 'avg'
        
        Empty dataset statistics:
        >>> ... # Test empty processor returns count=0, others None
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
        >>> ... # Test processor with name "dataset_123" returns True
        
        Invalid characters (should raise ValueError with message "Invalid dataset name"):
        >>> ... # Test processor with name "data@set!" raises ValueError
        """
        import re
        if not re.match(r'^[a-zA-Z0-9_]+$', self.dataset_name):
            raise ValueError("Invalid dataset name")
        return True
    
    def get_creation_time(self):
        """Return creation timestamp.
        
        Timestamp format:
        >>> ... # Test creation time is float like 1234567890.123...
        """
        return self.created_at
    
    def reset(self):
        """Clear all values and reset processor.
        
        Reset functionality:
        >>> ... # Test that after adding values and reset(), values list is empty
        """
        self.values = []
        return True