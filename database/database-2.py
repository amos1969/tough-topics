my_table = {10: ["Dave", "Bolton", 49],
            201: ["Andy", "Cookley", 47],
            31: ["Liz", "Willenhall", 70],
            265: ["Connor", "Bolton", 13]
            }

def search_for_primary_key(key):
    return_value = ""
    try:
        return_value = my_table[key]
    except KeyError:
        return_value = "Key not found"
    return return_value

def search_for_data_in_table(item):
    keys = []
    for key in my_table:
        if item in my_table[key]:
            keys.append(key)
    return keys

print(search_for_data_in_table("Karen"))
