# Prefix-to-Postfix Converter

## Description

A command-line tool for converting prefix expressions to postfix notation using stack-based processing. 
It reads expressions from an input file, processes them, and writes the results to an output file. 
Optionally, performance metrics can be recorded. It supports:

- Batch Processing: Read multiple expressions from an input file.
- Performance Tracking: Measure execution time and memory usage.
- Error Handling: Detect invalid expressions and provide error messages for diagnostics.

## Input format

Input strings need to be passed in with a .txt file (input_file). Each line of the input file contains one prefix to proces.
- The characters that will be processed include digits, alphabets, and the following symbols: +, -, *, /, $, ^
- The symbol "^" will be automatically converted to "$", the default symbol for exponential in this package.
- A number need to be separated with a blank space if followed by another number. e.g., 2 33, otherwise the package will consider the digits as belonging to the same number.

## Output file

The output file contains each input string being process and its corresponding output. If an error raised during processing, the error will appear as the output.
Summary statistics on the total and average time and peak memory used to process the input strings.

## Performance tracking (optional)

When the optional parameter for saving performance tracking is used, a .txt file will be saved that include the performance for processing each input string in the file.
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

```bash
git clone https://github.com/yixian625/data-structure
cd your-repo/lab1
```

## Execution

Run the package from the command line using:

```bash
python -m lab1 <input_file> <output_file> [--perf <performance_file>]
```

## Author

Project Maintainer: Yixian Li
Email: yli708@jh.edu
GitHub: https://github.com/yixian625