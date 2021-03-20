import sys
import sqlite3
from sqlite3 import Error


def create_connection(db_file:str = None):
    """ create a database connection to a SQLite database """
    if db_file is None:
        raise Exception("No database file name!")
        

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

            

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"short.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS shorts (
                                        short text PRIMARY KEY,
                                        url text NOT NULL,
                                        datetime int,
                                        hits integer
                                    ); """
    try:
        # create a database connection
        conn = create_connection(database)
        if conn is None:
            raise Exception("Error! cannot create the database connection")
    except Error as e:
        print(e)
        sys.exit()

    try:
       # create projects table
        create_table(conn, sql_create_projects_table)
    except Error as e:
        print(e)
        sys.exit()

if __name__ == '__main__':
    main()