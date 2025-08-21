# by @redfurie

import tkinter as tk
from tkinter import messagebox
import random

someWords = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'avocado', 'watermelon', 'blueberry', 'coconut', 'pear', 'apricot']
word = random.choice(someWords) # randomly choose a word

def handle_guess():
    global chances, correct, letterGuessed, word_display
    # user input
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    # parse input
    if not guess.isalpha():
        messagebox.showerror("Error", "Enter only a LETTER please!")
        return
    elif len(guess) > 1:
        messagebox.showerror("Error", "Enter only a SINGLE letter please!")
        return
    elif guess in letterGuessed:
        messagebox.showerror("Error", "You already guessed that letter!")
        return

    # handle guess
    letterGuessed += guess
    if guess in word:
        correct += word.count(guess)
        word_display = ''.join([letter if letter in letterGuessed else '_' for letter in word])
        word_label.config(text=word_display)
        if correct == len(word):
            messagebox.showinfo("Congratulations", "You guessed the word!")
            root.quit()
    else:
        chances -= 1
        chances_label.config(text=f"Chances left: {chances}")
        if chances == 0:
            messagebox.showinfo("Game Over", f"You have run out of chances! The word was '{word}'.")
            root.quit()

if __name__ == '__main__':
    # set up the window
    root = tk.Tk()
    root.title("Hangman Game")

    tk.Label(root, text="Welcome to Hangman game. Guess the word! HINT: the word is a fruit").pack()

    word_display = '_ ' * len(word)
    word_label = tk.Label(root, text=word_display)
    word_label.pack()

    tk.Label(root, text="Enter a letter to guess:").pack()
    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Guess", command=handle_guess)
    button.pack()

    chances_label = tk.Label(root, text=f"Chances left: {len(word) + 2}")
    chances_label.pack()

    letterGuessed = ''
    chances = len(word) + 2
    correct = 0

    root.mainloop()