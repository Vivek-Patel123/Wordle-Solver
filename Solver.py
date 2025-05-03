def solver():
    wrong_letters = set()
    possible_words = set()
    misplaced_letters = set()
    misplaced_positions = []
    right_letters = ["*","*","*","*","*"]

    while True:
        word = input("Enter First Word: ")
        if word.isalpha() and len(word) == 5:
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

        for i, letter in enumerate(pattern):
            if pattern[i] == "f":
                wrong_letters.add(word[i])
            if pattern[i] == "g":
                right_letters[i] = word[i]
            if pattern[i] =="y":
                misplaced_letters.add(word[i])
                misplaced_positions.append((word[i], i))
        
        with open("words.txt") as file:
            possible_words = set()
            for candidate in file:
                candidate = candidate.strip().lower()
                if len(candidate) == 5 and valid_word(candidate, pattern, wrong_letters, right_letters, misplaced_letters, misplaced_positions):
                    possible_words.add(candidate)
        
        word = possible_words.pop()
        print(f"Try this word {word}")

        while True:
            pattern = input("Enter the pattern: ")
            if valid_pattern(pattern):
                break
            else:
                print("\nPlease enter a valid pattern")


def valid_word(word, pattern, wrong_letters, right_letters, misplaced_letters, misplaced_positions):
    if set(word) & wrong_letters:
        return False

    if not misplaced_letters.issubset(set(word)):
        return False
    
    for i, letter in enumerate(pattern):
        if word[i] != right_letters[i] and right_letters[i] != "*":
            return False
        
    for letter, idx in misplaced_positions:
        if word[idx] == letter:
            return False   
        
    return True


def valid_pattern(word):
    return set(word).issubset({'g', 'y', 'f'})

if __name__ == "__main__":
    solver()