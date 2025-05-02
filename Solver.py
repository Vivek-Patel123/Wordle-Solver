def solver():
    steps = 0
    wrong_letters = set()
    possible_words = set()

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


    while True:
        if (pattern) == "ggggg":
            print("Good job!")
            exit(0)
        
        with open("words.txt") as file:
            for word in file:
                if len(word) == 5 and valid_word(word, pattern):
                    possible_words.add(word)
        
        print(f"Try this word {possible_words.pop()}")

        while True:
            pattern = input("Enter the pattern: ")
            if valid_pattern(pattern):
                break
            else:
                print("\nPlease enter a valid pattern")


def valid_word(word, pattern):



def valid_pattern(word):
    return set(word).issubset({'g', 'y', 'f'})

if __name__ == "__main__":
    solver()