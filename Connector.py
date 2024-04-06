import mysql.connector

class Connector:
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = "kps@3115"
        self.database = "colmonsys"

        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL database successfully!")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)

if __name__ == "__main__":
    Connector()
