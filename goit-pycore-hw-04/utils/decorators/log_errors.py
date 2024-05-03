def log_errors(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      print(f'{log_errors.__name__}: {e}')
  return wrapper