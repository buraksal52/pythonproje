def reverse_list(lst):

  result = []
  for item in reversed(lst):
    if isinstance(item, list):
      result.append(reverse_list(item))
    else:
      result.append(item)
  return result

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)  # Çıktı: [[7, 6, 5], [4, 3], [2, 1]]