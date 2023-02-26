from xml.dom import minidom

from logic import create_list
from logic import get_defs
from logic import get_contexts

word = input(">>> Intodu un cuvant:\n")
file_name = word + ".xml"

full_list = create_list(word)
defs = get_defs()
contexts = get_contexts()

annotations = {}

for item in full_list:
    print("\nCONTEXT: " + contexts[item])
    for index, definition in enumerate(full_list[item]):
        print("\t " + str(index) + ": " + defs[definition][0])

    print("\n")
    number = input(">>> Intodu numarul definitiei corecte:\n")

    if not number == "skip" and 0 < int(number) < len(full_list[item]) - 1:
        annotations[item] = full_list[item][int(number)]

full_annotations = {}
for anno in annotations:
    if annotations[anno] in full_annotations:
        full_annotations[annotations[anno]].append(anno)
    else:
        full_annotations[annotations[anno]] = [anno]

root = minidom.Document()

xml = root.createElement('goldCorpus')
root.appendChild(xml)

for anno in full_annotations:
    instance = root.createElement('instance')
    instance.setAttribute('id', "RoWordNet." + anno)
    instance.setAttribute('docsrc', "ROWN")
    xml.appendChild(instance)

    for index, value in enumerate(full_annotations[anno]):
        context = root.createElement("context")
        context.setAttribute('id', str(index))
        context.appendChild(root.createTextNode(contexts[value]))
        instance.appendChild(context)


xml_str = root.toprettyxml(indent ="\t")

with open(file_name, "w", encoding="utf-8") as f:
    f.write(xml_str)
