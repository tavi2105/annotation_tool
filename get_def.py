import xml.etree.cElementTree as ET

tree = ET.parse('rown.xml')
root = tree.getroot()


def get_def_entries(word):
    entries = {}
    for child in root.findall("./SYNSET/SYNONYM/[LITERAL='" + word + "']..."):
        if child.find('ID').text in entries:
            entries[child.find('ID').text].append(child.find('DEF').text)
        else:
            entries[child.find('ID').text] = [word + " | POS: " + child.find('POS').text
                                              + " | ID: " + child.find('ID').text + " | > " + child.find('DEF').text]

    return entries
