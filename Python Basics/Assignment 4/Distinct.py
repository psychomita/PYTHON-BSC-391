def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
list = [1, 1, 1, 24, 5, 7, 3, 3, 5, 8, 9, 0, 9]
print("Original list :\n",list)
print("New list with distinct elements :\n",unique_list(list))
