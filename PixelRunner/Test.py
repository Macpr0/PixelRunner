# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
secret_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    if guess_count == 3:
        print("You used all your Chances!")

secret_number = 10
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
    if guess_count == guess_limit:
        print("You used all your Chances!")
        break
prices = ["apple", "banana", "watermelon"]

for element in prices:
    print(element)
# 1, 2, 3, 4, 5
c = list(range (1,5))
print(c)

list = [1, 2, 3]
for element in list:
    print(element)

numbers = [5,2,5,2,2]
for f in numbers:
  print("x" * f)

  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
  for item in matrix:
      for row in item:
          print(row)

  numbers = [1, 2, 3, 6, 1]
  max = numbers[0]
  for number in numbers:
      if number > max:
          max = number
          print(max)

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
    if guess_count >= guess_limit:
        print("You lose!")


        def car_game():
            command = ""
            while True:
                command = input(">").lower()
                if command == "start":
                    print("Car starting...Car Ready to go!")
                elif command.lower() == "stop":
                    print("Car stopped")
                elif command == "help":
                    print("""start - to start the Car
        stop - to stop the Car
        quit - to Exit
                    """)
                elif command.lower() == "quit":
                    break
                else:
                    print("I don´t understand that!")


#sfasfasf
        phone = input("Phone: ")
        digits_mapping = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four"
        }
        output = ""
        for ch in phone:
            output += digits_mapping.get(ch, "!") + " "
        print(output)

    command = ""
    start = False
    stop = False
    while True:
        command = input(">").lower()
        if command == "start".lower():
            if start:
                print("Car already started!")
            else:
                start = True
                print("Car Starting...Ready to go!")
        elif command == "stop".lower():
            if stop:
                print("Car already stopped!")
            else:
                stop = True
                print("Car stopped")
        elif command == "help".lower():
            print("""start - to start the car
    stop - to stop the car
    quit - to quit the game""")
        elif command == "quit".lower():
            break
        else:
            print("I don´t understand that!")

            secret_number = 10
            guess_count = 0
            guess_limit = 3
            while guess_count < guess_limit:
                command = int(input("Guess: "))
                guess_count += 1
                if command == secret_number:
                    print("You Won!")
                    break
                elif guess_count == guess_limit:
                    print("You used all of your Chances!")
car_game()


import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)

