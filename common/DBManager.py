import psycopg2


# Singleton DBManager
class DBManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBManager, cls).__new__(cls)
            cls.__init__(cls._instance)
        return cls._instance

    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            dbname='bienes_raices',
            user='postgres',
            password='leo2002',
            port=5432)
        self.c = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, values):
        self.c.execute(f"INSERT INTO {table_name} VALUES ({values})")
        self.conn.commit()

    def select(self, table_name, columns, condition):
        self.c.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.c.fetchall()

    def update(self, table_name, columns, condition):
        self.c.execute(f"UPDATE {table_name} SET {columns} WHERE {condition}")
        self.conn.commit()

    def delete(self, table_name, condition):
        self.c.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def execute(self, query):
        self.c.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()
