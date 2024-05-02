from random import randint

def are_parameters_valid(min, max, quantity):
    is_min_valid = min >= 1
    is_max_valid = max <= 1000
    is_quantity_valid = quantity >= 1
    is_range_valid = max >= min
    is_quantity_in_range = quantity <= (max - min + 1)

    return is_min_valid and is_max_valid and is_quantity_valid and is_range_valid and is_quantity_in_range
    
def get_numbers_ticket(min, max, quantity=5):
      if not are_parameters_valid(min, max, quantity):
        return []
      
      numbers = set()
      
      while len(numbers) < quantity:
            numbers.add(randint(min, max))
            
      return sorted(list(numbers))
      