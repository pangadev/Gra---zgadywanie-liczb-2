print("Think about number from 1 - 1000 and I will try to guess it in 10 steps!")

def guess():
    words = {
        "too_big_number": ["too big", "Too big", "less", "Smaller", "smaller"],
        "too_small_number": ["too small", "Too small", "more", "Bigger", "bigger"],
        "win": ["Yes", "yes", "Super!", "You won"],
        "no": ["NO", "no", "No", "nope", "Nope"]
    }
    results = []
    moves = 0
    min = 0
    max = 1000
    while moves < 10:
        guess = int((max - min) / 2) + min
        results.append(str(guess))
        results1 = ', '.join(results)
        print(f"I'm guessing... {guess}!")
        z = input("Did I've guessed? ")
        if z in words["win"]:
            print("I've won!")
            moves = 10
            print(f"Tried numbers: {results1}")
        elif z in words["no"]:
            z = input("Is the number smaller or bigger? ")
            moves += 1
            print(f"Moves made: {moves}")
            if z in words["too_small_number"]:
                min = guess
            elif z in words["too_big_number"]:
                max = guess
        else:
            print("Do not cheat!")

guess()