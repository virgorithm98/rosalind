def count_word_occurrence(file_path: str) -> str:
    counted_words = {}
    with open(file_path, 'r') as text_in:
        for line in text_in:
            for word in line.split(" "):
                counted_words.update({word: counted_words[word] + 1} if word in counted_words else {word : 1})

    for key, value in counted_words.items():
        print(key, value)


count_word_occurrence("../data/ini_6_sample_text_1.txt")