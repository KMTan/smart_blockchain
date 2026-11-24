import json

def sort_character(data):
    chars = [char for char in json.dumps(data)]
    sorted_chars = sorted(chars)
    return ''.join(sorted_chars)



