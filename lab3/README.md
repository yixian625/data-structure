# Huffman Encoding and Decoding

## Description
This is a command-line tool for Huffman encoding/decoding. It reads a source file that contains either a frequency table
or source texts to generate the frequency table from, builds the Huffman encoding tree based on the source file, and processes
messages based on the generated Huffman encoding tree. 

Please note that this package only supports English alphabets. Any character that is not an alphabet is ignored.

Key functions supported:

- *Tree Description*: save the tree structure in preorder and the encoding for each letter.
- *Encoding*: encode plain text messages using Huffman encoding based on the source file.
- *Decoding*: decode binary messages encrypted using the Huffman encoding based on the source file.
- *Compression rate tracking*: for each encoded text, measure how much the text is compressed by encoding.

## Input files

- **Source file**: a .txt file containing either a frequency table or paragraphs of plain text to use to build the frequency
table from. 
  - The frequency table must follow the format of "letter - freq" (e.g., A - 10), with each letter and its
  frequency on a separate line.
  - The plain text paragraphs must contain all letters in the alphabets.
- **File to encode**: a .txt file that contains plain English texts to be encoded using the Huffman encoding system built 
using the source file.
- **File to decode**: a .txt file that contains the binary messages to be decoded using the Huffman encoding system built
using the source file.

## Output files

- **Tree map file**: a .txt file saved under the user-specified name that describes the Huffman encoding tree generated based
on the source file. It contains the tree structure traversed in preorder, as well as the binary encoding for each letter.
- **Encoded result file**: a .txt file saved under the user-specified name that contains the encoded version of the messages
in the *File to encode* input file. The size of original vs. encrypted version and a compression rate is also stored for each message in the file.
- **Decoded result file**: a .txt file saved under the user-specified name that contains the decoded version of the messages in
the *File to decode* input file.

## Prerequisites

Python 3.10+

## Installation

Use the provided zip to extract the package locally. 

Alternatively you can clone the repository with

```
git clone https://github.com/yixian625/data-structure
cd your-repo/lab3
```

## Execution

Run the package in the command line using:

```chatinput
python -m lab3 <source file> <file to encode> <file to decode> <tree map file> <encoded result file> <decoded result file>
```

for example:
```chatinput
python -m lab3 FreqTable.txt ClearText.txt Encoded.txt TreeMap.txt EncodedRes.txt DecodedRes.txt
```

## Development Environment

- python version: 3.13
- PyCharm 2024.1.4 (Community Edition)

## Author

Project Maintainer: Yixian Li
Email: yli708@jh.edu
GitHub: https://github.com/yixian625