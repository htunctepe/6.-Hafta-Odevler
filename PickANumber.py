print("\nPick a number between 1-100. I'll try to guess the number.")
message = """
Is the number you guessed {}?

Enter 'y' if it is,
Enter '+' if the number I guessed is too small
Enter '-' if the number I guessed is too big  : """
control = ''
max = 101
min = 1
guess = int((max - min)/2) # Here basically starting with 50, this way the number possibilities will be halved
times = 0
try:
    while control != 'y':
        times += 1
        control = input(message.format(guess))
        if control == '-':
            max = guess         # Here we make sure the next guesses will definitely be smaller than our guess
        elif control == '+':
            min = guess         # Here we make sure the next guesses will definitely be bigger than our guess
        else:
            print("\nThe number you guessed is {}. The number is guessed at {}. time.".format(guess, times))
        guess = int((max + min)/2)

except ValueError:
    print("Wrong entry!")