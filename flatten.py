def flatten(array):
  new_arr = []

  for i in array:
    if type(i) is list:
      new_arr += flatten(i)
    else:
      new_arr.append(i)
      
  return new_arr