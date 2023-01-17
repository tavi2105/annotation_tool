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
                                        lemma text NOT NULL,
                                        head text NOT NULL
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_contexts_table)
    else:
        print("Error! cannot create the database connection.")


def create_context(conn, context):
    sql = ''' INSERT INTO contexts(id,context,lemma,head)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, context)
    conn.commit()

    return cur.lastrowid


def select_word(conn, word):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contexts WHERE (head=? OR lemma=?) AND adnoted=false LIMIT 1", (word, word,))

    rows = cur.fetchall()

    return rows


if __name__ == '__main__':
    main()
