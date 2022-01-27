from datetime import datetime
from threading import Lock
from database import Database


class Sqlite(Database):

    def __init__(self):
        self.db_admin = Database.connect(self)
        self.lock = Lock()

    # Add message to database
    def add_message(self, name, content, creation_time='default'):
        if creation_time == 'default':
            creation_time = datetime.now().strftime("%Y/%m/%d, %H:%M")
        add_message_query = "INSERT INTO messages (name, content, created_at) VALUES (?,?,?)"
        self.lock.acquire(True)
        self.db_admin.execute(add_message_query, (name, content, creation_time))
        self.lock.release()
        self.connection.commit()
