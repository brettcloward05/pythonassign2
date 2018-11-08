#!/usr/bin/env python3
"""
This program lists the top 25 errors from the specified log file
"""
from __future__ import print_function
import urllib.request
import sys
import re


def top_error(link):
    """
    Counts all the errors from the specified URL and
    lists the top 25 errors.
    Args:
        link: string the user inputs
    """
    error_file = urllib.request.urlopen(link)
    counts = {}
    # Go through the file and filter it so only the page is left
    for line in error_file:
        convert = (line.decode("utf-8"))
        filtered = re.search(r"(/var[a-zA-Z0-9/.]+)", convert)
        if filtered != None:
            key = filtered.group(0)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1

    order_list = list(counts.values())
    order_list.sort(reverse=True)
    errors = 0
    print("*** Top 25 page errors ***")
    while len(counts) > 0 & len(counts) < 26:
        next_value = order_list[0]
        if errors > 25:
            break
        errors += 1
        for key, value in counts.items():
            if value == next_value:
                print("Count: " + str(value) + " Page: " + str(key))
                order_list = order_list[1:]
                counts.pop(key)
                break


def user_help():
    """
    Provides usage  help to the user if input is --help or input is missing
    """
    print("usage is : brett_cloward_hw6.py <file input>")
    exit(1)


def main():
    """
    Test your module
    """
    if len(sys.argv) == 1:
        user_help()
    elif str(sys.argv[1]) == "--help":
        user_help()
    else:
        link = sys.argv[1]
        top_error(link)


if __name__ == "__main__":
    main()
    exit(0)
