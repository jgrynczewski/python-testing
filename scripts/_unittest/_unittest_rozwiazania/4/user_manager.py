import sqlite3
import os


class UserManager:
    """Manage users in SQLite database."""
    
    def __init__(self, db_path="users.db"):
        """Initialize with database path."""
        self.db_path = db_path
    
    def create_user(self, name, email):
        """Create new user. Returns user ID."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id
    
    def get_user(self, user_id):
        """Get user by ID. Returns dict or None."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        return None
    
    def delete_user(self, user_id):
        """Delete user by ID. Returns True if deleted."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted
    
    def user_exists(self, email):
        """Check if user with email exists."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0


if __name__ == "__main__":
    manager = UserManager("example.db")
    
    # Create database table first
    conn = sqlite3.connect("example.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.close()
    
    # Create new user
    user_id = manager.create_user("John Doe", "john@example.com")
    print(f"Created user with ID: {user_id}")
    
    # Get user
    user = manager.get_user(user_id)
    print(f"Retrieved user: {user}")
    
    # Check if user exists
    exists = manager.user_exists("john@example.com")
    print(f"User exists: {exists}")
    
    # Delete user
    deleted = manager.delete_user(user_id)
    print(f"User deleted: {deleted}")
    
    # Cleanup
    os.remove("example.db")