def fetch_data(path: str, callback: callable = None) -> list | None:
  try:
    with open(path, 'r', encoding='utf-8') as file:
      unstructured_data = file.readlines()
      if not unstructured_data:
        raise ValueError(f"{fetch_data.__name__}: файл порожній. Будь ласка, перевірте контент файлу.")
      if callable(callback):
        return callback(unstructured_data)
      else:
        return [line.strip() for line in unstructured_data]
  except FileNotFoundError:
    raise FileNotFoundError(f"{fetch_data.__name__}: файл не знайдено. Перевірте шлях до файлу.")