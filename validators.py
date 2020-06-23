def validate_number(word):
    if word[0] == '-':
        return True
    return word.isdigit()


def validate_string(word):
    return word.isalpha()


def is_list_empty(cur_list):
    return len(cur_list) == 0
