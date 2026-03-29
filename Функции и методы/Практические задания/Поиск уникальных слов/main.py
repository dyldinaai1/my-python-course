def get_unique_words(text):
    words = text.split()
    unique_words = set(words)
    result = list(unique_words)
    result.sort()
    return result


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
