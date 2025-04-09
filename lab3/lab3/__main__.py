# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports.

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
import sys
#
from lab3.lab3 import process_file

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("freq_table", type=str, help="Frequency Table File Pathname")
arg_parser.add_argument("to_encode_file", type=str, help="File Pathname for Texts to Encode")
arg_parser.add_argument("tree_map", type=str, help="Huffman Encoding Tree Map File Pathname")
arg_parser.add_argument("encode_result", type=str, help="File Pathname to store the encoding results")

# # Optional argument for saving performance tracking file
# arg_parser.add_argument("-p", "--perf", type=str, help="Performance File Pathname")
#
# # Optional argument for converting to infix instead of postfix
# arg_parser.add_argument("-f", "--format", choices= ['in', 'post'],
#                         default='post',
#                         help=f"Which format the output takes ('in' for infix or 'post' for postfix)."
#                              f"Default to postfix.")

args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
freq_table_path = Path(args.freq_table)
to_encode_path = Path(args.to_encode_file)
tree_map_path = Path(args.tree_map)
encode_res_path = Path(args.encode_result)
# perf_path = Path(args.perf) if args.perf else None
# out_format = args.format

if not freq_table_path.exists():
    print(f"No {args.freq_table} exists. Please choose another input file.")
    sys.exit(1)

process_file(freq_table_file=freq_table_path, to_encode_file=to_encode_path, tree_map_file=tree_map_path,
             encode_res_file=encode_res_path)


# process_file(input_path=in_path, output_path=out_path, out_format = out_format, perf_path=perf_path)
