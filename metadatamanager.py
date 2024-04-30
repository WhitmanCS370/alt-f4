import sqlite3

class MetadataManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT,
                value TEXT,
                length TEXT,
                last_modified TEXT,
                description TEXT,
                tags TEXT
            )
        ''')
        self.conn.commit()

    # add a new metadata item for a sound
    def add(self, key, value, length, last_modified, description, tags):
        self.cursor.execute('''
            INSERT INTO metadata (key, value, length, last_modified, description, tags) VALUES (?, ?, ?, ?, ?, ?)
        ''', (key, value, length, last_modified, description, tags))
        self.conn.commit()

    def list(self):
        self.cursor.execute('''
            SELECT key, value FROM metadata
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()