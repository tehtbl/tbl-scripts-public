#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
This script fixes all csv exports from deutsche bank website for later
importing into local finance tools.
"""

import os
import re
import io
import csv
import sys
import chardet

#
# print help and exit
#
def help():
    print("Usage: %s <FILE>" % sys.argv[0])
    sys.exit(1)

#
# convert_line
#
def convert_account(row):
    row_len = len(row)

    new_row = {
        'date': row[0],
        'contact': " ".join(row[2:4]),
        'combined_desc': ' '.join(row[4:row_len-3]).replace('"', '').strip(),
        'diff': row[row_len-2] if len(row[row_len-2]) > 0 else row[row_len-3],
        'currency': row[row_len-1],
    }

    # new_row['diff'] = list(new_row['diff'].replace(',', '.'))
    # new_row['diff'][-3] = ','
    # new_row['diff'] = "".join(new_row['diff'])

    return new_row

#
# MAiN
#
if __name__ == "__main__":

    # Check that a filename is passed
    try:
        in_filename = sys.argv[1]
    except:
        help()

    # Read stdin in binary mode
    in_file_b = open(in_filename, "rb").read()

    # Guess encoding
    in_file_enc = chardet.detect(in_file_b)

    # Attempt decoding
    in_file_s = in_file_b.decode(in_file_enc["encoding"])

    # Set convert method
    convert = convert_account

    # Filter out the garbage
    csv_lines = []
    for line in in_file_s.split("\n"):
        if re.match("^\d+\.\d+\.\d+;", line):
            csv_lines.append(line)

    csv_s = "\n".join(csv_lines)

    # Parse as a CSV file
    reader = csv.reader(io.StringIO(csv_s), delimiter=";")

    # Prepare to write to stdout
    writer = csv.writer(sys.stdout, delimiter=";")

    # Write CSV header
    writer.writerow(["Date", "Payee", "Category", "Memo", "Outflow", "Inflow"])

    # Convert all lines and output
    for row in reader:
        writer.writerow((convert(row)).values())
