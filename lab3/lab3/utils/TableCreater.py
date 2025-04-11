# functions to help create a frequency table from an input file


def create_freq_table(text_file):

    """
    store the frequencies for each letter in a list
    the index of the letter is its ascii order - 65
    so that 0 is A and 25 is Z.
    :param text_file: source to create freq table from
    :return: the list of frequencies for all letters from A to Z contained in the source text
    """

    freq_array = [0]*26

    for line in text_file:
        for char in line:
            if char.isalpha():
                char_index = ord(char.upper()) - 65
                freq_array[char_index] += 1

    return freq_array


def detect_table(text_file):
    """
    Detects whether the text file is a freq table or a source text
    :param text_file: input file
    :return: "Table" or "Text"
    """
    # check the first two lines to see if the file is in
    first_line = text_file.readline()
    second_line = text_file.readline()
    text_file.seek(0)  # return to the beginning of the file

    # if the first two lines both conform to the format of a
    # freq table file, then we consider it to be a freq table
    try:
        first = first_line.strip().split(" - ")
        second = second_line.strip().split(" - ")

        if first[0].isalpha() and first[1].isdigit() and \
                second[0].isalpha() and second[1].isdigit():
            return "Table"
        else:
            return "Text"
    except Exception as e:
        return "Text"





