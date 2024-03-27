#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_statistics(total_size, status_counts):
    """
    print_statistics method
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


def parse_line(line):
    """
    parse_line method
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code.isdigit():
            return int(status_code), int(file_size)
    return None, None


def main():
    """
    main function
    """
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
