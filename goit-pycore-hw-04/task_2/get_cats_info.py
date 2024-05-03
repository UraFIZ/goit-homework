import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.file_operations.fetch_data import fetch_data
from utils.decorators.log_errors import log_errors

def transform_cat_list_to_dictionary(data: list) -> list:
    cat_dictionary = []
    for line in data:
        parts = line.split(',')
        if len(parts) != 3:
            raise ValueError(f"{transform_cat_list_to_dictionary.__name__}: cкладнощь з опрацюванням строки: {line}. Кожна строка має містити (id, name, age).")
        elif "" in [part.strip() for part in parts]:
            raise ValueError(f"{transform_cat_list_to_dictionary.__name__}: cкладношь з опрацюванням строки: {line}. Кожен елемент має містити значення. Пуста строка недозволяється.")
        else:
            cat_dictionary.append({"id": parts[0], "name": parts[1], "age": parts[2].strip()})
    return cat_dictionary
  
@log_errors
def get_cats_info(path):
  cats_list = fetch_data(path, transform_cat_list_to_dictionary)
  print(cats_list)

get_cats_info('cats_file.txt')