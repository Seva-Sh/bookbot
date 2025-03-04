def words_count(str):
    return len(str.split())

def sort_on(dict):
    x = list(dict.values())
    return x[0]

def chars_count(str):
    chars_dict = {}
    

    for char in str:
        current_char = char.lower()
        if current_char in chars_dict:
            chars_dict[current_char] += 1
        else:
            chars_dict[current_char] = 1
    
    return chars_dict

def chars_sort(dict):
    chars_list = []

    for c in dict:
        chars_list.append({c: dict[c]})

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list