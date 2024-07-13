import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_phonebook = [contacts_list[0]]

for i in range(1, len(contacts_list)):
    res = " ".join(contacts_list[i][:3]).strip().split(" ")

    name_list = []
    for item in res:
        if item:
            name_list.append(item)

    for name in name_list:
        if name not in new_phonebook:
            new_phonebook.append([
                name_list[0], name_list[1], name_list[2] if len(name_list) > 2 else " ",
                contacts_list[i][3], contacts_list[i][4], contacts_list[i][5], contacts_list[i][6]
            ])

pattern = r"(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*([доб\.]*)\s*(\d{4})?\)*"
pattern_comp = re.compile(pattern)
substring = r"+7(\2)\3-\4-\5 \6\7"

for i in range(1, len(new_phonebook)):
    result = pattern_comp.sub(substring, new_phonebook[i][5])
    new_phonebook[i][5] = result


def remove_duplicates(data):
    remove_dict = {}
    for j in data[1:]:
        key = (j[0], j[1])
        if key in remove_dict:
            if j[2] != " ":
                remove_dict[key][2] = j[2]
            if j[3]:
                remove_dict[key][3] = j[3]
            if j[4]:
                remove_dict[key][4] = j[4]
            if j[5]:
                remove_dict[key][5] = j[5]
            if j[6]:
                remove_dict[key][6] = j[6]
        else:
            remove_dict[key] = j
    return [data[0]] + list(remove_dict.values())


if __name__ == '__main__':
    remove_data = remove_duplicates(new_phonebook)
    pprint(remove_data)
    with open("new_phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(remove_data)
