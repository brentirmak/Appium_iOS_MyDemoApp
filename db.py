import mysql.connector
import os
import datetime
from mysql.connector import Error

class MySQLLogger:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.conn = None
        self.cursor = None

    def connect(self):
        """Create the connection only when needed."""
        if self.conn is None:
            print(f"[MySQLLogger] Connecting to {self.host} as {self.user}")

            try:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                self.cursor = self.conn.cursor()
                print("[MySQLLogger] Connection established")

            except Error as e:
                print(f"[MySQLLogger] Connection failed: {e}")
                raise

        return self.conn

    def log_result(self, test_name, status, duration, error_message):
        """Insert a test result into the database."""
        self.connect()

        query = """
            INSERT INTO appium_ios_mydemoapp (test_name, status, duration, error_message, executed_at)
            VALUES (%s, %s, %s, %s, %s)
        """

        self.cursor.execute(query, (test_name, status, duration, error_message, datetime.datetime.now()))
        self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
