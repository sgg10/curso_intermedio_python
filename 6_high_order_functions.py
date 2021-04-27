from functools import reduce

def run():
  my_list = [1,4,5,6,9,13,19,21]

  # Filter
  odd = list(filter(lambda x: x%2 != 0, my_list))
  print(odd)

  # Map
  squares = list(map(lambda x: x**2, my_list))
  print(squares)

  # Reduce
  all_multiply = reduce(lambda a, b: a * b, my_list)
  print(all_multiply)


if __name__ == '__main__':
  run()