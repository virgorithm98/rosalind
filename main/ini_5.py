def rewrite_even_numbered_line(file_path_load: str, file_path_save: str):
    """
    This function will read all the lines from a text file and rewrite another file which contains the even-numbered line from the text source
    :param file_path_load: The path of a source text file
    :param file_path_save: The path of where the new file is going to be saved
    :return: None
    """

    with open(file_path_load, 'r') as text_in:
        with open(file_path_save, 'w') as text_out:
            for number, line in enumerate(text_in, start=1):
                if number % 2 == 0:
                    text_out.write(line)


rewrite_even_numbered_line("../data/sample_text_1.txt", "../data/sample_text_2.txt")