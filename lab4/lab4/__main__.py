# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports.

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
import sys

from lab4.lab4 import process_file

# # Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_folder", type=str, help="Pathname for Freq Table or Source Text to Build Freq Table From")
arg_parser.add_argument("tracking_file", type=str, help="Pathname for File Storing the Number of Comprisons and Swaps")
arg_parser.add_argument("--returnSorted", choices=['yes', 'no'], default='no',
                        help="Whether to return the sorted results or not. Default to no. If yes, the outputs will be automatically saved \
                             with the name of the sorting algorithm in file name")
arg_parser.add_argument("--upMaxRecur", choices=['yes', 'no'], default='no',
                        help="Whether to set the recursion limit of python to 10,050 to allow all methods to run successfully.\
                         Default to no. Use with caution. The limit will be automatically reset after the runs.")

args = arg_parser.parse_args()
#
# # pathlib.Path is also a fantastic built in tool and has a lot of great
# # features. Please look it up! I promise it's worth it.
input_folder_path = Path(args.input_folder)
tracking_file_path = Path(args.tracking_file)

if not input_folder_path.exists():
    print(f"No {args.input_folder_path} exists. Please double check the folder path.")
    sys.exit(1)

# Loop through all .txt files
txt_files = list(input_folder_path.glob("*.txt"))
if not txt_files:
    print(f"No .txt files found in {input_folder_path}. Please make sure your inputs are all .txt files")
    sys.exit(1)

# up the python recursion max limit if wanted
original_recur_max = sys.getrecursionlimit()
if args.upMaxRecur == 'yes':
    sys.setrecursionlimit(10050)

# run all sorting on all the .txt files in the folder
tracker = []

save_sorted = True if args.returnSorted == 'yes' else False
for txt_file in txt_files:
    try:
        input_size, file_order, sort_type, time_cost, num_compares, num_swaps = process_file(txt_file, return_sorted = save_sorted)
        tracker.append((input_size, file_order, sort_type, time_cost, num_compares, num_swaps))
    except Exception as e:
        print(f'Program error encountered: {e} for file: {txt_file}')
        print(f'Skipping this input.')
        pass

with open(tracking_file_path, 'w') as tracking:
    tracking.write("Input Size | Input Order | Sort Type| Time (ms) | Num Comparisons | Num Swaps\n")
    for input_size, file_order, sort_type, time_cost, num_compares, num_swaps in tracker:
        for i in range(0, len(sort_type)):
            tracking.write(f"{input_size} | {file_order} | {sort_type[i]} | {time_cost[i]*1000: .2f} | {num_compares[i]} | {num_swaps[i]}\n")

# reset the recursion limit to original
sys.setrecursionlimit(original_recur_max)
