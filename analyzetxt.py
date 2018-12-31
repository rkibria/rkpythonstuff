#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Count words in a text file
"""

import os
import time
import math
import string
import argparse

def round_to_decimals(num, decs):
    """
    Round floating point number to some number of decimals
    """
    factor = math.pow(10.0, decs)
    return math.trunc(num * factor) / factor

def measure_time(func):
    """
    Time measuring decorator
    """
    def measure_time_wrapper(*args, **kwargs):
        starttime = time.time()
        result = func(*args, **kwargs)
        takentime = time.time() - starttime
        print('* took {} sec'.format(round_to_decimals(takentime, 3)))
        return result
    return measure_time_wrapper

@measure_time
def load_contents(filename):
    """
    Load text file into a flat list, return list and number of lines
    """
    print('Loading file {}, size is {} bytes'.format(filename, os.path.getsize(filename)))
    contents = []
    nlines = 0
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            nlines += 1
            words = line.split()
            contents.extend(words)
    print('Found {} words in {} lines'.format(len(contents), nlines))
    return (contents, nlines)

@measure_time
def count_words(contents):
    """
    Returns dictionary of words and their count.
    Removes all punctuation characters.
    """
    print("Count words")
    counts = {}
    for word in contents:
        word = word.lower()
        word = word.translate(str.maketrans("", "", string.punctuation))
        if not word in counts:
            counts[word] = 0
        counts[word] += 1
    return counts

@measure_time
def sort_counts(counts):
    """
    Sorting
    """
    print("Sorting by count")
    countofwords = [(count, word) for word, count in counts.items()]
    sortedcounts = sorted(countofwords, reverse=True)
    return sortedcounts

def main():
    """
    Entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="path to text file")
    parser.add_argument("--simple", help="just output the words without statistics",
                        action="store_true")
    args = parser.parse_args()

    contents, _nlines = load_contents(args.filename)
    counts = count_words(contents)
    sortedcounts = sort_counts(counts)

    for i in range(min(len(sortedcounts), 1000)):
        count, word = sortedcounts[i]
        if not args.simple:
            percentage = round_to_decimals(count / float(len(contents)) * 100.0, 3)
            print('#{}: {} ({}, {}%)'.format(i + 1, word, count, percentage))
        else:
            print(word)

if __name__ == '__main__':
    main()
