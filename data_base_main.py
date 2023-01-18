import sqlite3
from sqlite3 import Error


def create_connection(db_file=r"data/pythonsqlite.db"):
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
    sql_create_contexts_table = """ CREATE TABLE IF NOT EXISTS contexts (
                                        id text PRIMARY KEY,
                                        context text NOT NULL,
                                        lemma text NOT NULL,
                                        head text NOT NULL
                                    ); """

    sql_create_annotation_table = """ CREATE TABLE IF NOT EXISTS annotations (
                                        id text PRIMARY KEY,
                                        wordnet_id text NOT NULL,
                                        context text NOT NULL,
                                        context_id text NOT NULL
                                    ); """

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_contexts_table)
        create_table(conn, sql_create_annotation_table)
    else:
        print("Error! cannot create the database connection.")


def create_context(conn, context):
    sql = ''' INSERT INTO contexts(id,context,lemma,head)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, context)
    conn.commit()

    return cur.lastrowid


def create_annotation(conn, wn_id, context, context_id):
    counter = select_anno_count(conn, wn_id)

    sql = ''' INSERT INTO annotations(id,wordnet_id,context,context_id)
                  VALUES(?,?,?,?) '''
    update_context_sql = '''UPDATE contexts SET annotated=true WHERE id=?'''
    cur = conn.cursor()
    cur.execute(sql, (wn_id + str(counter), wn_id, context, context_id))
    cur.execute(update_context_sql, (context_id,))
    conn.commit()

    return cur.lastrowid


def select_anno_count(conn, wn_id):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM annotations WHERE wordnet_id=?", (wn_id,))

    counter = cur.fetchall()

    return counter[0][0]


def select_word(conn, word):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contexts WHERE (head=? OR lemma=?) AND annotated=false LIMIT 1", (word, word,))

    rows = cur.fetchall()

    return rows


if __name__ == '__main__':
    main()
