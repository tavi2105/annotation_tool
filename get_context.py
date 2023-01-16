import requests
from html.parser import HTMLParser

import re

corpora_entries = {}


class MyHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.left_good = False
        self.word_good = False
        self.right_good = False
        self.li_name = ""
        self.more = False

    def handle_starttag(self, tag, attrs):
        if ('class', 'context-left') in attrs:
            self.left_good = True
        elif ('class', 'match') in attrs:
            self.word_good = True
        elif ('class', 'context-right') in attrs:
            self.right_good = True
        elif ('class', 'more') in attrs:
            self.more = True
        elif tag == "li":
            self.li_name = attrs[1][1] + "/" + attrs[0][1]

    def handle_endtag(self, tag):
        if not self.more:
            self.left_good = False
        self.more = False
        self.word_good = False
        self.right_good = False

    def handle_data(self, data):
        global corpora_entries
        data = " ".join(data.split())
        if data != "":
            if self.left_good:
                corpora_entries[self.li_name] = data

            elif self.word_good:
                corpora_entries[self.li_name] = corpora_entries[self.li_name] + " <head>" + data + "</head> "

            elif self.right_good:
                corpora_entries[self.li_name] = corpora_entries[self.li_name] + " " + data


def extract_from_html_corpora(word):
    html = requests.get("https://korap.racai.ro/?q=" + word)

    parser = MyHTMLParser()
    parser.feed(html.text)


def get_from_all_pages(word, page_index=1):
    len_before = len(corpora_entries)
    extract_from_html_corpora(word + "&p=" + str(page_index))
    len_after = len(corpora_entries)
    if len_before != 50:
        get_from_all_pages(word, page_index + 1)


def get_contexts(word):
    get_from_all_pages(word)
    return corpora_entries


get_contexts("nouă")

for i in corpora_entries:
    html = requests.get("https://korap.racai.ro/corpus/" + i)

    span = re.compile(r'<mark><span title="drukola/l:[a-zăîâșț]+">')
    print(span.search(html.text).group().split(":")[1][:-2])

print(len(corpora_entries))




