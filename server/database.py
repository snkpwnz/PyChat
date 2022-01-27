from sqlite3 import connect


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Database(Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = connect('new_db', check_same_thread=False)
            self.cursorobj = self.connection.cursor()
        try:
            create_table_messages_query = '''CREATE TABLE messages(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    name TEXT NOT NULL,
                                    content INT NOT NULL,
                                    created_at timestamp NOT NULL
                                    );'''

            self.cursorobj.execute(create_table_messages_query)

        except Exception:
            pass
        return self.cursorobj