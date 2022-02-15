import random
def guess_num():
    name, cnt, rand = input('Hello! What is your name?\n'), 1, random.randint(1, 20)
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess')
    n = int(input())
    if n == rand: print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
    else:
        while n != rand:
            if n < rand:
                print('Your guess is too low.\nTake a guess')
            else:
                print('Your guess is too big.\nTake a guess')
            cnt += 1
            n = int(input())
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
guess_num()