#!/usr/bin/env python3
import time

file_path = 'monitored_file.txt'

for i in range(1, 6):
    msg = f"Line {i}: hiiii"
    print(msg, flush=True)
    with open(file_path, 'a') as file:
        file.write(msg + '\n')
    time.sleep(2)
