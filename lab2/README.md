# Prefix-to-Postfix Converter

## Description

A command-line tool for converting prefix expressions to postfix or infix notation using recursive functions. 
It reads expressions from an input file, processes them, and writes the results to an output file. The default output format is postfix, but the user can optionally ask for infix outputs.
There is also an option to document the performance metrics for each input string. It supports:

- Batch Processing: read multiple expressions from an input file.
- Performance Tracking: measure execution time and peak memory usage for each string processed.
- Error Handling: detect invalid expressions and provide error messages for diagnostics.

## Input file format

Input strings need to be passed in with a .txt file. Each line of the input file contains one prefix to process.
- The characters that can be processed include alphabets and the following symbols: +, -, *, /, $, ^
- The symbol "^" will be automatically converted to "$", the default symbol for exponential in this package.

## Output file

The output file contains each input string being process and its corresponding output. If an error raised during processing, the error will appear as the output.
Summary statistics are saved to the end of the output file, reporting the total and average time and peak memory used to process the input strings.

The default output expression is postfix, but the user can use the -f or --format flag with *in* as the parameter to get infix expression as output.

## Performance tracking (optional)

When the optional parameter for performance tracking is used, a .txt file will be saved that includes the performance for processing each input string in the file.
Information tracked include: 
- the string
- the number of characters in the string 
- time (ms) used to process the string (to completion or until an error raises)
- peak memory (kb) used when processing the string 
- completion status: success or encountering an error 

## Prerequisites

Python 3.10+

## Installation

Use the provided zip to extract the package locally. 

Alternatively you can clone the repository with

```
git clone https://github.com/yixian625/data-structure
cd your-repo/lab2
```

## Execution

While in the lab2 folder, run the package from the command line using:

### For getting postfix as output
```
python -m lab2 <input_file> <output_file> [--perf <performance_file>]
```
### for getting infix as output
```
python -m lab2 <input_file> <output_file> [--format in] [--perf <performance_file>]
```

## Development Environment

- python version: 3.13
- PyCharm 2024.1.4 (Community Edition)

## Author

Project Maintainer: Yixian Li
Email: yli708@jh.edu
GitHub: https://github.com/yixian625