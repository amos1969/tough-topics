my_table = { 1: ["Dave", "Bolton", "25/05/1969"],
             2: ["Andy", "Cookley", "02/05/1971"],
             3: ["Karen", "Doncaster", "03/08/1969"],
             4: ["Connor", "Bolton", "02/03/2005"]}

def search_on_primary_key(key, table):
    if key in table:
        the_data = table[key]
    else:
        the_data = "Record not found"
    return the_data

def search_for_item_in_data(search_term, table):
    keys = []
    for key in table:
        if search_term in table[key]:
            keys.append(key)
    return keys



#print(search_on_primary_key(5, my_table))
print(search_for_item_in_data("Bolton", my_table))