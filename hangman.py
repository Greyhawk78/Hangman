# Write your code here
import random
targets_list = ['python', 'java', 'kotlin', 'javascript']
hidden_list = list(random.choice(targets_list))
shown_list = []
used_char=set()
lives = 8


def create_empty():
    for i in range(0, len(hidden_list)):
        shown_list.append('-')


def legal_input(char):
    if len(char) != 1:
        print("You should input a single letter")
        return False
    if char not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a lowercase English letter")
        return False
    if char in used_char:
        print("You've already guessed this letter")
        return False
    else:
        used_char.add(char)
    return True


def checking_input():
    char = input('Input a letter:')
    found = False
    if not legal_input(char):
        return True
    for ix in range(0, len(hidden_list)):
        if hidden_list[ix] == char and shown_list[ix] != char:
            shown_list[ix] = char
            found = True
        elif hidden_list[ix] == char and shown_list[ix] == char:
            print("No improvements")
            return False
    if not found:
        print("That letter doesn't appear in the word")
        return False
    return True


def output_screen():
    print()
    print(''.join(shown_list))


def play_game():
    global lives
    while True:
        output_screen()
        if not checking_input():
            lives = lives - 1
        if lives == 0:
            print('You lost!\n')
            break
        if hidden_list == shown_list:
            output_screen()
            print("You guessed the word!\nYou survived!\n")
            break


create_empty()
print("H A N G M A N")
while True:
    print('Type "play" to play the game, "exit" to quit:')
    decision = input()
    if decision == 'play':
        play_game()
    if decision == 'exit':
        break



