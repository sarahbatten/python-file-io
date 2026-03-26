#!/usr/bin/env python3

# importing the necessary modules for using regular expressions

import re

"""
The purpose of this script is to iterate over each line of the in_stream, origin.txt to find all each instance where "herit" is used in a word. 

Parameters
----------
in_stream: this is a file object that will be searched for the regular expression of interest, "herit".

herit_pattern: a regular expression object that is the target patter of in_stream

Output
------
A tuple that contains the object that matches the regular expression. Each time an object that matches the regular expression is found, a tuple is created that has the regular expression match and the line number on which it is found. This is saved in a file called output.txt.

"""


if __name__ == "__main__":
    herit_pattern_str = r'\w*herit\w*'
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)

    print('Opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('Opening output.txt')
        with open('output.txt', 'w') as out_stream:
            for line_num, line in enumerate(in_stream, start=1):
                line = line.strip()
                word_list = line.split()

                for word in word_list:
                    if herit_pattern.search(word):
                        output = f"{line_num}: {word}"
                        print(output)
                        out_stream.write(output + '\n')
    print("Done!")
    print('origin.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)
