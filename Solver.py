def solver():
    steps = 0
    wrong_letters = set()

    while True:
        first_word = input("Enter First Word: ")
        if first_word.isalpha() and len(first_word) == 5:
            break
        else:
            print("\nPlease enter a valid word")

    while True:
        pattern = input("Enter the pattern: ")
        if valid_pattern(pattern) and len(pattern) == 5:
            break
        else:
            print("\nPlease enter a valid pattern")


def valid_pattern(word):
    return set(word).issubset({'g', 'y', 'f'})

if __name__ == "__main__":
    solver()