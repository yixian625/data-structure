# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports.

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
import sys

from lab3.lab3 import process_file

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")

# Optional argument for saving performance tracking file
arg_parser.add_argument("-p", "--perf", type=str, help="Performance File Pathname")

# Optional argument for converting to infix instead of postfix
arg_parser.add_argument("-f", "--format", choices= ['in', 'post'],
                        default='post',
                        help=f"Which format the output takes ('in' for infix or 'post' for postfix)."
                             f"Default to postfix.")

args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path = Path(args.in_file)
out_path = Path(args.out_file)
perf_path = Path(args.perf) if args.perf else None
out_format = args.format

if not in_path.exists():
    print(f"No {args.in_file} exists. Please choose another input file.")
    sys.exit(1)

process_file(input_path=in_path, output_path=out_path, out_format = out_format, perf_path=perf_path)
