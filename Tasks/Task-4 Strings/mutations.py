def mutate_string(string, position, character):
    lst_str = list(string)
    lst_str[position] = character
    string = ''.join(lst_str)
    return string

