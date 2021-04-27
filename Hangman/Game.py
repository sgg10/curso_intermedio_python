from Menu import Menu, Instructions
from Steps import draw_man
import os
from random import choice

def readWords():
  with open("./data.txt", "r", encoding="utf-8") as file:
    return [line.replace("\n", "") for line in file]

def configureWord(word):
  hide_word = ["_" for _ in range(len(word))]
  index = { i:[] for i in word }
  for key in index.keys():
    for i in range(len(word)):
      if key == word[i]:
        index[key].append(i)
  return hide_word, index

def draw(step):
  os.system("clear")
  draw_man(step)

def game(word):
  hide_word, index = configureWord(word)
  attempts = 0
  while "".join(hide_word) != word and attempts < 6:
    draw(attempts)
    print(" ".join(hide_word))
    attempt = input("Please enter a letter: ")

    if attempt in word:
      if attempt in hide_word:
        continue

      for i in index[attempt]:
        hide_word[i] = attempt
    else:
      attempts += 1

  if attempts == 6:
    draw(attempts)
    print(f"The word was {word}")
    print("Game over ❌😢")
  elif "".join(hide_word) == word:
    print(f"The word is {word}")
    print("You win 🔥👍✌")
  input("Press any key to continue...")


def run():
  os.system("clear")
  option = Menu()
  words = readWords()
  while option != "9":
    if option == "1":
      game(choice(words))
    elif option == "2":
      Instructions()
    os.system("clear")
    if option != "9":
      option = Menu()

if __name__ == '__main__':
  run()