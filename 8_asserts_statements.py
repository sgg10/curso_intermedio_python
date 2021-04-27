divisors = lambda number: [i for i in range(1, number+1) if number % i == 0]

def run():
  num = input('Ingrese un número: ')
  assert num.isnumeric(), "Debes ingresar un número"
  assert int(num) >= 0, "Debes ingresar un número positivo"
  print(divisors(int(num)))

if __name__ == '__main__':
  run()