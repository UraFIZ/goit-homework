import sys
import os
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from collections import defaultdict
from utils.file_operations.fetch_data import fetch_data

def parse_log_line(line: str) -> dict:
    parts = line.split()
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': ' '.join(parts[3:])
    }

def fetch_data_callback(filter_level: str = None) -> callable:
  def fetch_data_from_file(file):
    if filter_level:
      return [parse_log_line(line) for line in file if line.strip() and (not filter_level or parse_log_line(line)['level'] == filter_level.upper())]
    return [parse_log_line(line) for line in file if line.strip()]
  return fetch_data_from_file


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

def display_filtered_logs(logs: list):
    print("Логі:")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
        
def validate_log_level(level: str = None):
    if not level:
        return None
    valid_levels = {'INFO', 'ERROR', 'DEBUG', 'WARNING'}
    if level.upper() not in valid_levels:
        raise ValueError(f"Не вірний рівень лога '{level}'. Правельні рівні: INFO, ERROR, DEBUG, WARNING (можно писати і lowercase).")
    return level


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використовуйте наступний патерн: python script.py <log_file_path> [log_level]")
        sys.exit(1)
    try:
        filter_level = validate_log_level(sys.argv[2] if len(sys.argv) > 2 else None)
    except ValueError as e:
        print(e)
        sys.exit(1)
  
    logs = fetch_data(sys.argv[1], fetch_data_callback(filter_level))

    if logs:
        if filter_level:
            print(f"Деталі по логам на рівні '{filter_level.upper()}':")
            display_filtered_logs(logs)
        else:
            counts = count_logs_by_level(logs)
            display_log_counts(counts)
    else:
        sys.exit(1)
