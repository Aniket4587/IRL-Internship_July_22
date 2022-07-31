def count_substring(string, sub_string):
    ct=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            ct+=1
    return ct

