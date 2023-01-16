import sqlite3
from sqlite3 import Error


def create_connection(db_file=r"pythonsqlite.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
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
    database = r"pythonsqlite.db"

    sql_create_contexts_table = """ CREATE TABLE IF NOT EXISTS contexts (
                                        id text PRIMARY KEY,
                                        context text NOT NULL,
                                        lemma text NOT NULL
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_contexts_table)
    else:
        print("Error! cannot create the database connection.")


def create_context(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO contexts(id,context,lemma)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


if __name__ == '__main__':
    main()
