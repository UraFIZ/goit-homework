def log_errors(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      print(f'Декаратор {log_errors.__name__} виявив наступну помилку в {e}')
  return wrapper