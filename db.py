import datetime

import mysql.connector

class MySQLLogger:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def log_result(self, test_name, status, duration, error_message=None):
        query = """
            INSERT INTO appium_mydemoapp (test_name, status, duration, error_message, executed_at)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (test_name, status, duration, error_message,datetime.datetime.now()))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()