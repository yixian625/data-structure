# print("a".isalpha())
#
# print("A" + "ABC+" + "/")
#
# # with open("resources/input/Required-Input.txt", 'r') as file:
# #     for line in file:
# #         for char in line:
# #             print(repr(char))
# print("112 ".isdigit())

import os
print(os.getcwd())

with open("resources/input/Required-input.txt") as file:
    for line in file:
        print(repr(line))
        for char in line:
            print(repr(char))
        print("\n\n")

