import sqlite3
import datetime

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
                length INTEGER,
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
        ''', (key, value, length, self.getTimeStamp(), description, tags))
        self.conn.commit()

    def list(self):
        self.cursor.execute('''
            SELECT key, value FROM metadata
        ''')
        return self.cursor.fetchall()

    def add_tags(self, filename, tags):
        self.cursor.execute('''
            UPDATE metadata SET tags = ?, last_modified = ? WHERE key = ?
        ''', (tags, self.getTimeStamp(), filename))
        self.conn.commit()

    def add_description(self, filename, description):
        self.cursor.execute('''
        UPDATE metadata SET description = ?, last_modified = ? WHERE key = ?
        ''', (description, self.getTimeStamp(), filename))
        self.conn.commit()

    def search_by_tag(self, tag):
        search_pattern = f'%{tag}%'  # This creates a pattern to match the tag anywhere in the string
        self.cursor.execute('''
        SELECT key, value FROM metadata WHERE tags LIKE ?
        ''', (search_pattern,))
        return self.cursor.fetchall()

    def set(self, key, value):
        self.cursor.execute('''
            INSERT INTO metadata (key, value) VALUES (?, ?)
        ''', (key, value))
        self.conn.commit()

    def get(self, key):
        self.cursor.execute('''
            SELECT value FROM metadata WHERE key = ?
        ''', (key,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return row[0]

    def close(self):
        self.conn.close()

    def getTimeStamp():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")