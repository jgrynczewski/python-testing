import os


class RealFileHandler:
    """Real file handler using standard Python file operations."""
    
    def read(self, filename):
        """Read file content."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write(self, filename, data):
        """Write data to file. Returns True on success."""
        try:
            with open(filename, 'w') as f:
                f.write(data)
            return True
        except:
            return False
    
    def exists(self, filename):
        """Check if file exists."""
        return os.path.exists(filename)
    
    def get_size(self, filename):
        """Get file size in bytes."""
        return os.path.getsize(filename)


class FileProcessor:
    """Process files using dependency injection for external file operations."""
    
    def __init__(self, file_handler):
        """Initialize processor with file handler."""
        self.file_handler = file_handler
    
    def process_text(self, filename):
        """Read text file and convert to uppercase."""
        content = self.file_handler.read(filename)
        return content.upper()
    
    def save_data(self, filename, data):
        """Save data to file and return success status."""
        return self.file_handler.write(filename, data)
    
    def copy_file(self, source, destination):
        """Copy file from source to destination."""
        content = self.file_handler.read(source)
        return self.file_handler.write(destination, content)
    
    def safe_read(self, filename):
        """Safely read file. Returns None if file doesn't exist."""
        try:
            return self.file_handler.read(filename)
        except FileNotFoundError:
            return None
    
    def get_file_info(self, filename):
        """Get file info. Returns dict with exists and size."""
        exists = self.file_handler.exists(filename)
        if exists:
            size = self.file_handler.get_size(filename)
        else:
            size = 0
        
        return {"exists": exists, "size": size}


if __name__ == "__main__":
    handler = RealFileHandler()
    processor = FileProcessor(handler)
    
    # Create test file
    with open("test_input.txt", "w") as f:
        f.write("hello world")
    
    # Convert text to uppercase
    result = processor.process_text("test_input.txt")
    print(f"Processed: {result}")
    
    # Save data to file
    success = processor.save_data("output.txt", "Hello World")
    print(f"Save successful: {success}")
    
    # Copy file
    copy_success = processor.copy_file("test_input.txt", "copy.txt")
    print(f"Copy successful: {copy_success}")
    
    # Safe read (missing file)
    content = processor.safe_read("nonexistent.txt")
    print(f"Safe read result: {content}")
    
    # Get file info
    info = processor.get_file_info("test_input.txt")
    print(f"File info: {info}")
    
    # # Cleanup
    # os.remove("test_input.txt")
    # os.remove("output.txt")
    # os.remove("copy.txt")