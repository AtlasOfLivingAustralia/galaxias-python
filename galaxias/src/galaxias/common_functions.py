import pandas as pd

def snake_to_camel_case(list_of_words=None):

    new_list = []
    for w in list_of_words:
        term = w.lower().split("_")
        for i in range(len(term)):
            term[i] = term[i].capitalize()
        new_list.append("".join(term))
    return new_list