import re

string_to_count = "I have an IR project to complete."

def word_count_func(string_to_count):
    word_list = re.findall("\w+", string_to_count)
    str_length = len(word_list)
    #print(str_length)
    return str_length
    #print(len(word_list))

#word_count(string_to_count)
