import sqlite3

# Step 1: Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("match_data.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

# Step 4: Insert sample data
cursor.execute("""
INSERT INTO users (name, age, email)
VALUES ('Alice', 30, 'alice@example.com')
""")

# Step 5: Commit changes and close the connection
connection.commit()
connection.close()

print("Database setup complete!")