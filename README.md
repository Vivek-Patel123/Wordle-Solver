# 🟩 Wordle Solver (Python)

A simple Python program that helps you solve the game [Wordle](https://www.nytimes.com/games/wordle/index.html) using pattern-based logic and letter elimination.

---

## 🎯 What is Wordle?

[Wordle](https://www.nytimes.com/games/wordle/index.html) is a word-guessing game developed by the New York Times.  
Each day, players have **6 attempts** to guess a secret **5-letter English word**.

After each guess, the game provides feedback for each letter:
- 🟩 **Green**: The letter is correct and in the correct position.
- 🟨 **Yellow**: The letter is in the word but in the wrong position.
- ⬛ **Gray**: The letter is not in the word at all.

---

## 💡 About This Project

This Python script acts as an intelligent **Wordle assistant**.  
It narrows down the list of possible words based on your previous guesses and the color-coded feedback you receive.

---

## 🛠️ Features

- Tracks:
  - ✅ Correct letters in the correct spot (green)
  - 🔁 Letters in the word but misplaced (yellow)
  - ❌ Letters not in the word at all (gray)
- Suggests valid next guesses based on logic and feedback
- Uses a dictionary (`words.txt`) of possible 5-letter English words
- Handles invalid inputs and user-friendly prompts

---

## 🚀 How to Run

1. Clone this repository or download the script.
2. Make sure you have Python 3 installed.
3. Place a `words.txt` file in the same folder, with a list of valid 5-letter words (one per line).
4. Run the solver:
   ```bash
   python wordle_solver.py
