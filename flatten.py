def flatten(array):
  flattened = []
  for el in array:
    if type(el) is list:
      flatten(el)
    else:
      flattened += el
  return flattened