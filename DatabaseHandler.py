import sqlite3

class DatabaseHandler:

    def __init__(self):
        pass

    def establishConnection(self):
        conn = sqlite3.connect('movieTracks.db')
        return conn

    def getCursor(self, conn):
        return conn.cursor()

    def query(self, c, query):
        c.execute(query)

    def initAll(self):
        conn = self.establishConnection()
        c = self.getCursor(conn)

        self.query(c, '''CREATE TABLE IF NOT EXISTS users ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
        [login_name] text, [password] text, [display_name] text)''')

        self.query(c, '''CREATE TABLE IF NOT EXISTS users_movies ([user_id] INTEGER,
        [movie] text, [favourite] INTEGER, [score] INTEGER, [status] text, [poster_path] text,
        PRIMARY KEY(user_id, movie),
        FOREIGN KEY(user_id) REFERENCES users(id))''')

        conn.commit()
        conn.close()