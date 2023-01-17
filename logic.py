from get_def import get_def_entries
from data_base_main import create_connection, select_word

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

    list_of_contexts = []
    for context in all_contexts:
        defs = get_def_entries(context[2])
        list_of_contexts.append({
            "id": context[0],
            "context": context[1],
            "lemma": context[2],
            "definitions": defs
        })

    json = {
        "word": word,
        "definitions": list_of_contexts
    }

    print(json)

    return json


create_list('banca')
