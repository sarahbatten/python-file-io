#!/usr/bin/env python3

import re

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
                        output = f"Line {line_num}: {word}"
                        print(output)
                        out_stream.write(output + '\n')
    print("Done!")
    print('origin.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)
