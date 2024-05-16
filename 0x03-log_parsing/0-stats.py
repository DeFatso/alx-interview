#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_count = {}


def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        # Split the input line by space
        parts = line.split()
        if len(parts) != 10:
            continue

        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            else:
                status_code_count[status_code] = 1

        # Increment line count
        line_count += 1

        # Check if it's time to print statistics
        if line_count == 10:
            print_statistics()
            line_count = 0

except KeyboardInterrupt:
    print_statistics()
