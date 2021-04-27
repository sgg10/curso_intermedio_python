def run():
  my_list = [i**2 for i in range(101) if i % 3 != 0]

  numbers= [i for i in range(100000) if i % 36 == 0]

  print(numbers)

if __name__ == '__main__':
  run()