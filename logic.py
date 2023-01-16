from get_context import extract_from_html_corpora
from get_def import get_def_entries

dict_contexts = {}
def_entries = {}


def get_list():
    all_forms = {}
    for context in dict_contexts:
        for entry in def_entries:
            if context in all_forms:
                all_forms[context].append(entry)
            else:
                all_forms[context] = [entry]

    return all_forms


def get_contexts():
    return dict_contexts


def get_defs():
    return def_entries


def create_list(word):
    global dict_contexts
    global def_entries
    extract_from_html_corpora(word)
    def_entries = get_def_entries(word)

    list_word = list(word)
    if word[-1] == "a":
        list_word[-1] = "ă"
    elif word[-1] == "ă":
        list_word[-1] = "a"
    elif word[-2:] == "ul":
        list_word.pop()
        list_word.pop()
    else:
        list_word.append("ul")

    word = "".join(list_word)

    extract_from_html_corpora(word)
    def_entries.update(get_def_entries(word))

    list_word = list(word)

    list_word.append("ă")

    word = "".join(list_word)
    all_contexts = extract_from_html_corpora(word)
    print(len(all_contexts))

    dict_contexts = {}
    for index, value in enumerate(all_contexts):
        dict_contexts[index] = value

    return get_list()
