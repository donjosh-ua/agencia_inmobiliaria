import psycopg2


def make_connection():
    connection = psycopg2.connect(
        user="postgres",
        password="postgres1234",
        host="localhost",
        port="5432",
        database="postgres"
    )
    return connection


def run():
    connection = make_connection()
    cursor = connection.cursor()

    if connection:
        print("Connection successful")

    cursor.close()
    connection.close()


run()