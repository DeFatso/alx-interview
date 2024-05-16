#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_code_count = {}

def print_statistics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue
        
        file_size = int(parts[-1])
        status_code = parts[-2]

        total_file_size += file_size

        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            else:
                status_code_count[status_code] = 1

        line_count += 1

        if line_count == 10:
            print_statistics()
            line_count = 0

except KeyboardInterrupt:
    print_statistics()
