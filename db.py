# db.py
import os
import mysql.connector
from mysql.connector import Error

class MySQLLogger:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        """Create the connection only when needed."""
        if self.conn is None:
            host = os.getenv("MYSQL_URL")
            user = os.getenv("MYSQL_USERNAME")
            password = os.getenv("MYSQL_PASSWORD")

            print(f"[MySQLLogger] Connecting to {host} as {user}")

            try:
                self.conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password
                )
                self.cursor = self.conn.cursor()
                print("[MySQLLogger] Connection established")
            except Error as e:
                print(f"[MySQLLogger] Connection failed: {e}")
                raise

        return self.conn

    def log(self, message):
        """Example logging method."""
        self.connect()
        query = "INSERT INTO logs (message) VALUES (%s)"
        self.cursor.execute(query, (message,))
        self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
