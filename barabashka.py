def analyze_text(text):
    text = ''.join(char for char in text if char.isalpha() or char.isspace()).lower()
    words = text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words
def display_result(sorted_words):
    for word, count in sorted_words:
        print(f"{word}: {count}")
if __name__ == "__main__":
    input_text = input("Введите текст для анализа: ")
    result = analyze_text(input_text)
    display_result(result)
#задачо номир 2
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted_str1 = sorted(list(str1))
    sorted_str2 = sorted(list(str2))
    return sorted_str1 == sorted_str2
if __name__ == "__main__":
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    if are_anagrams(str1, str2):
        print("Эти строки являются анаграммами.")
    else:
        print("Эти строки не являются анаграммами.")
#задачо номир 3
def udalitt_slova(s):
    unique_bukvi = []
    for char in s:
        if s.count(char) == 1:
            unique_bukvi.append(char)
    return ''.join(unique_bukvi)
if __name__ == "__main__":
    input_string = input("Введите строку: ")
    result = udalitt_slova(input_string)
    print("Результат:", result)


