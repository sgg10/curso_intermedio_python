def Menu():
  return input("""
  🔥🎮 Hangman 🎮🔥
    1. Play
    2. Instructions
    9. Exit
  Choose an option: """)

def Instructions():
  return input("""
  📃 Instructions
    1. You must choose a letter at random
    2. You must guess the word
    3. You can't be wrong more than 6 times
  Press any key to continue...""")