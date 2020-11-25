import csv
from typing import List


def largest_string_chain(this_chain_of_words: List[str]) -> int:
    this_chain_of_words.sort(key=lambda x: len(x))

    words_dictionary = {}
    max_chain_from_letters = 0

    for available_word in this_chain_of_words:
        iterator_of_start = 0
        current_max_word = 1
        while iterator_of_start < len(available_word):
            possible_next_word = available_word[:iterator_of_start] + available_word[iterator_of_start + 1:]
            iterator_of_start = iterator_of_start + 1
            if possible_next_word in words_dictionary:
                current_max_word = max(current_max_word, words_dictionary[possible_next_word] + 1)
        words_dictionary[available_word] = current_max_word
        max_chain_from_letters = max(max_chain_from_letters, current_max_word)

    return max_chain_from_letters


def read_date_from_csv_file():
    this_date = []
    with open("input.csv") as input_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        next(csv_reader)
        for line in csv_reader:
            this_date.append(line[0])
        print(this_date)
    return this_date


def read_input_date():
    this_date = []
    input()
    while True:
        word = input()
        if word == "":
            break
        this_date.append(word)
    print(this_date)
    return this_date


if __name__ == '__main__':
    words = read_input_date()

    print(largest_string_chain(words))
