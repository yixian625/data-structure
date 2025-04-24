# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports.

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
import sys
#
# from lab4.lab4 import process_file
#
# # Argument parser is an amazing tool. It's worth mastering
# arg_parser = argparse.ArgumentParser()
# arg_parser.add_argument("source_file", type=str, help="Pathname for Freq Table or Source Text to Build Freq Table From")
# arg_parser.add_argument("to_encode_file", type=str, help="File Pathname for Texts to Encode")
# arg_parser.add_argument("to_decode_file", type=str, help='ile Pathname for Encrypted Message to Decode')
# arg_parser.add_argument("tree_map", type=str, help="Huffman Encoding Tree Map File Pathname")
# arg_parser.add_argument("encode_result", type=str, help="File Pathname to Store the Encoded Results")
# arg_parser.add_argument("decode_result", type=str, help="File Pathname to Store the Decoded Results")
#
# args = arg_parser.parse_args()
#
# # pathlib.Path is also a fantastic built in tool and has a lot of great
# # features. Please look it up! I promise it's worth it.
# source_file_path = Path(args.source_file)
# to_encode_path = Path(args.to_encode_file)
# to_decode_path = Path(args.to_decode_file)
# tree_map_path = Path(args.tree_map)
# encode_res_path = Path(args.encode_result)
# decode_res_path = Path(args.decode_result)
#
# if not source_file_path.exists():
#     print(f"No {args.source_file} exists. Please choose another input file.")
#     sys.exit(1)
#
# process_file(source_file=source_file_path, to_encode_file=to_encode_path, to_decode_file= to_decode_path,
#              tree_map_file=tree_map_path, encode_res_file=encode_res_path, decode_res_file=decode_res_path)


