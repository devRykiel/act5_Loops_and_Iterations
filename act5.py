
#Part 1: Count Digits in a Number

num = input('Enter a number: ')

count = 0
for digit in num:
        count += 1

print(f'''The number has {count} digits.
      ''')


#Part 2: Number Guessing Game (Limited Tries)
secret = 18

for i in range(5):
    guess = int(input('Guess the number (1–20): '))

    if guess < secret:
        print('Too low!')
    elif guess > secret:
        print('Too high!')
    else:
        print('Correct! You guessed it.')
        break
else:
    print('Out of tries! The number was', secret)

