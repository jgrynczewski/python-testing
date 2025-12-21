import random
import time


class DataProcessor:
    """Process and analyze numerical data with validation."""
    
    def __init__(self, dataset_name):
        """Initialize processor with dataset name."""
        self.dataset_name = dataset_name
        self.values = []
        self.created_at = time.time()
    
    def add_value(self, value):
        """Add numeric value to dataset."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Value must be positive")
        self.values.append(value)
        return True
    
    def calculate_average(self):
        """Calculate average of stored values."""
        if not self.values:
            raise ValueError("No values to calculate")
        return sum(self.values) / len(self.values)
    
    def get_sample_data(self, size=3):
        """Generate sample data for testing."""
        return [random.randint(0, 10) for _ in range(size)]
    
    def get_statistics(self):
        """Return dataset statistics as dict."""
        if not self.values:
            return {"count": 0, "min": None, "max": None, "avg": None}
        
        return {
            "count": len(self.values),
            "min": min(self.values),
            "max": max(self.values), 
            "avg": self.calculate_average()
        }
    
    def validate_dataset_name(self):
        """Validate dataset name format."""
        import re
        if not re.match(r'^[a-zA-Z0-9_]+$', self.dataset_name):
            raise ValueError("Invalid dataset name")
        return True
    
    def get_creation_time(self):
        """Return creation timestamp."""
        return self.created_at
    
    def reset(self):
        """Clear all values and reset processor."""
        self.values = []
        return True