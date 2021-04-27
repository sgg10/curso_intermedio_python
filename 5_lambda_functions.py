def run():
  palindrome = lambda value: value == value[::-1]
  print(palindrome("oso"))

if __name__ == '__main__':
  run()