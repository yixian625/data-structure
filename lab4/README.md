# Sorting Performance Comparison

## Description
This is a command-line tool for measuring the performance of six different types of sorting methods. The module takes 
a folder pathname and batch process all the .txt files in the folder: it sorts numbers in each input file using the following
six sorting methods, and tracks the time cost, number of comparisons, and the number of swaps used by each method:
- **BasicMergeSort**: straight-forward merge sort;
- **NaturalMergeSort**: natural merge sort;
- **BasicQuickSort**: straight-forward quick sort, always using the first item in an array as the pivot;
- **QuickSortMedianOfThreePivot**: straight-forward quick sort, choosing the median value of the first, middle, and last item in the array as the pivot;
- **QuickSortWithInsertionUnder50**: quick sort until any sub-array's size decreased to 50 or below, then uses insertion sort to finish the sorting;
- **QuickSortWithInsertionUnder100**: quick sort until any sub-array's size decreased to 100 or below, then uses insertion sort to finish the sorting.

Key functions supported:

- *Batch processing*: process all suitable .txt files in the input folder path.
- *Performance tracking*: saves the performance of each sort for each input, given the input size and order.
- *Stores sorted files* (optional): automatically saves the sorted result by each method for each input file. Output file name maps input file name and sorting method name.

## Input files

- **input Folder**: Path to a folder contains all the input files to be run:
  - The input files must all be .txt files;
  - The input files must contain one input number on each line.
  - Find example input files in the *resources/inputs* folder.

## IMPORTANT NOTE ON INPUT SIZE

if any of your input files contains more than 1000 numbers, you will need to set the *--upMaxRecur* flag to *yes* to process these files. 
The sorting methods are implemented with recursions and files with size over 1000 will run into the max recursion error. 

When using the flag, the package will temporarily set the max limit for recursion in your Python environment to 10,050, which will allow the package to run file size up to 10,000 input number.
**Please note that this risks crushing your Python and potentially your computer. Please proceed with caution.** 

If the flag is not set (left as default), the package will try
to run all input files, but will return None for performance of any sorting method that failed due to max recursion error.

## Output files

- **Tracking File**: a .txt file name to save the performance comparison statistics to. 
  - Example tracking file: *resources/Example_tracking_file.txt*
  

- **Sorted Files** (optional): if the optional flag *--returnSorted* is set to *yes*, the package will save the sorted results for *each sort method* to
your current directory. The file names will contain the input file name and the name of the sorting method used to generate the output.
  - Example sorted files can be found in *resources/example outputs*


## Prerequisites

Python 3.10+

## Installation

Use the provided zip to extract the package locally. 

Alternatively you can clone the repository with

```
git clone https://github.com/yixian625/data-structure
cd your-repo/lab4
```

## Execution

Run the package in the command line using:

```chatinput
python -m lab4 <input folder path> <tracking file name> [--returnSorted yes/no] [--upMaxRecur yes/no]
```

for example:
```chatinput
python -m lab4 resources/inputs Tracking_results.txt --returnSorted yes --upMaxRecur yes
```

Both the --returnSorted and the --upMaxRecur flags are defaulted to no to facilitate efficient processing.

## Development Environment

- python version: 3.13
- PyCharm 2024.1.4 (Community Edition)

## Author

Project Maintainer: Yixian Li
Email: yli708@jh.edu
GitHub: https://github.com/yixian625