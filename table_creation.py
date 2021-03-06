# code from https://www.sqlitetutorial.net/sqlite-python/creating-tables/

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"db\database.db"

    sql_create_clients_table = """ CREATE TABLE IF NOT EXISTS clients (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                        ); """

    sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS movies (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                    );"""

    sql_create_rents_table = """ CREATE TABLE IF NOT EXISTS rents (
                                    id integer PRIMARY KEY,
                                    client_id integer NOT NULL,
                                    movie_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (client_id) REFERENCES clients (id),
                                    FOREIGN KEY (movie_id) REFERENCES movies (id)
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create clients table
        create_table(conn, sql_create_clients_table)

        # create movies table
        create_table(conn, sql_create_movies_table)

        # create rents table
        create_table(conn, sql_create_rents_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
