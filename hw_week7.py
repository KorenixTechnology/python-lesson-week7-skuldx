import random

def hw_week7(secret_number):
    try_count = 0
    result = (random.randint(1,100))

    while True:

        # For interactive input
        #secret_number = input('Take a guess.')

        if int(secret_number) > result:
            print('Your guess is too high.')
            try_count += 1

        elif int(secret_number) < result:
            print('Your guess is too low.')
            try_count += 1

        elif int(secret_number) == result:
            try_count += 1
            print('Good job!You guessed my number in ' + str(try_count) + ' guesses!')
            break

if __name__ == '__main__':
    hw_week7(random.randint(1, 100))
