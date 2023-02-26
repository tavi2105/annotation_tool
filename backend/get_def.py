import xml.etree.cElementTree as ET

tree = ET.parse('data/rown.xml')
root = tree.getroot()


def get_def_entries(word):
    entries = []
    for child in root.findall("./SYNSET/SYNONYM/[LITERAL='" + word + "']..."):
        entries.append({
            "word": word,
            "pos": child.find('POS').text,
            "id": child.find('ID').text,
            "def": child.find('DEF').text
        })

    return entries
