#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""

import sys
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()

        # Parse the line using split
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, _, _, status_code, file_size = parts[0], parts[5], parts[6]
        if not status_code.isdigit():
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
