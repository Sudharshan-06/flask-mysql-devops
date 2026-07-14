import mysql.connector
import os
import time


def get_db():

    db = None

    for i in range(10):
        try:
            db = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE"),
            )
            print("Connected to MySQL")
            return db

        except:
            print("Waiting for MySQL...")
            time.sleep(5)

    raise Exception("Could not connect to MySQL")