from math import sqrt

def run():
  my_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}

  challenge = {i: sqrt(i) for i in range(1,1001)}

  print(challenge)


if __name__ == '__main__':
  run()