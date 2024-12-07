def rewrite_even_numbered_line(file_path_load: str, file_path_save: str) -> str:
    """

    :param file_path:
    :return:
    """

    with open(file_path_load, 'r') as text_in:
        with open(file_path_save, 'w') as text_out:
            for number, line in enumerate(text_in, start=1):
                if number % 2 == 0:
                    text_out.write(line)


rewrite_even_numbered_line("../data/sample_text_1.txt", "../data/sample_text_2.txt")