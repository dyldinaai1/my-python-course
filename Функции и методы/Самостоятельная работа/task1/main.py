def remove_whitespace(text):
    result = ""
    prev_char_is_space = False
    for char in text:
        if char == " ":
            if not prev_char_is_space:
                result += char
                prev_char_is_space = True
        else:
            result += char
            prev_char_is_space = False
    return result



str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
