#!/usr/bin/env python3

# a library of utility functions for Rosalind exercises

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped


# Tims file import os:

import os # Used for global same directory call to "safeornot.txt"

# Global call to safeornot.txt
here = os.path.dirname(os.path.abspath(__file__))
safeornot = os.path.join(here, "FILENAME")