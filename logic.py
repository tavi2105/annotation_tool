from get_def import get_def_entries
from data_base_main import create_connection, select_word, create_annotation

dict_contexts = {}
def_entries = {}


def get_contexts():
    return dict_contexts


def get_defs():
    return def_entries


def create_list(word):
    global dict_contexts
    global def_entries
    conn = create_connection()

    all_contexts = select_word(conn, word)

    context = all_contexts[0]
    get_def_entries(word)
    defs = get_def_entries(context[2])

    json = {
        "word": word,
        "context_id": context[0],
        "context": context[1],
        "lemma": context[2],
        "definitions": defs
    }

    print(json)

    return json


def add_annotation(wn_id, context, context_id):
    conn = create_connection()
    create_annotation(conn, wn_id, context, context_id)
