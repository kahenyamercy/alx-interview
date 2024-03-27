#!/usr/bin/env python3

import sys

def print_stats(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 6:
                status_code = parts[-2]
                file_size = int(parts[-1])

                total_size += file_size

                if status_code.isdigit():
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                total_size = 0
                status_counts = {}

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
