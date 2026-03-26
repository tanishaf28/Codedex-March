"""
Given a nested list/array (one that can contain numbers or other lists/arrays), sometimes deeply nested, your task is to flatten it into a "single-level" list/array.
Complete the function that returns a new list/array with all values flattened.
"""
def flatten(my_lists):
  # Write code below 💖
  result = []
  for item in my_lists:
    if isinstance(item, list):
      result.extend(flatten(item))
    else:
      result.append(item)
  return result
