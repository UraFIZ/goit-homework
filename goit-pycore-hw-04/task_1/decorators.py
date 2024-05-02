def global_exception_handler(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      print(f'{global_exception_handler.__name__}: {e}')
  return wrapper