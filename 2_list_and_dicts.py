def run():
  my_list = ["Hello", 1, True, 4.5]
  my_dict = { "firstname": "Sebastian", "lastname": "Granda" }

  super_list = [
    { "firstname": "Valentina", "lastname": "Mora" },
    { "firstname": "Sebastian", "lastname": "Granda" },
    { "firstname": "Isaac", "lastname": "Hincapie" },
    { "firstname": "Camilo", "lastname": "Romero" },
  ]

  super_dict = {
    "natural_nums": list(range(1,6)),
    "integer_nums": list(range(-6, 6)),
    "float_nums": [1.1, 0.89, 15.85, 33.22]
  }

  for key, value in super_dict.items():
    print(f"{key} = {value}")

  for person in super_list:
    print(f"{person['firstname']} {person['lastname']}")

if __name__ == '__main__':
  run()