# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports.

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
import sys

from lab1.lab1 import process_file

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")

# Optional argument for saving performance tracking file
arg_parser.add_argument("-p", "--perf", type=str, help="Performance File Pathname")

args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path = Path(args.in_file)
out_path = Path(args.out_file)
perf_path = Path(args.perf) if args.perf else None

if not in_path.exists():
    print(f"No {args.in_file} exists. Please choose another input file.")
    sys.exit(1)

process_file(input_path=in_path, output_path=out_path, perf_path=perf_path)
