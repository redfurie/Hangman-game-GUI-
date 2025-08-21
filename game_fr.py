# by @redfurie

import tkinter as tk
from tkinter import messagebox
import random

someWords = ['pomme', 'banane', 'cerise', 'date', 'avocat', 'figue', 'raisin', 'kiwi', 'citron', 'mangue', 'mandarine', 'orange', 'poire', 'framboise', 'fraise', 'ananas', 'papaye', 'pastèque', 'myrtille', 'coco', 'cacao', 'goyave']
word = random.choice(someWords) # randomly choose a word

def handle_guess():
    global chances, correct, letterGuessed, word_display
    # user input
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    # parse input
    if not guess.isalpha():
        messagebox.showerror("Erreur, Veiller entrer une LETTRE svp!")
        return
    elif len(guess) > 1:
        messagebox.showerror("Erreur, Veiller entrer une SEULE LETTRE svp")
        return
    elif guess in letterGuessed:
        messagebox.showerror("Erreur, Vous avez déjà deviné cette lettre!")
        return

    # handle guess
    letterGuessed += guess
    if guess in word:
        correct += word.count(guess)
        word_display = ''.join([letter if letter in letterGuessed else '_' for letter in word])
        word_label.config(text=word_display)
        if correct == len(word):
            messagebox.showinfo("FELICITATION, vous avez deviné le mot!")
            root.quit()
    else:
        chances -= 1
        chances_label.config(text=f"Chances left: {chances}")
        if chances == 0:
            messagebox.showinfo("Game Over", f"Vous n'avez plus de chances restantes! Le mot était '{word}'.")
            root.quit()

if __name__ == '__main__':
    # set up the window
    root = tk.Tk()
    root.title("Hangman Game")

    tk.Label(root, text="Bienvenue dans 'Hangman game' version fruit. Devinez le mot! HINT: le mot est un fruit").pack()

    word_display = '_ ' * len(word)
    word_label = tk.Label(root, text=word_display)
    word_label.pack()

    tk.Label(root, text="Entrer une lettre pour deviner:").pack()
    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Deviner", command=handle_guess)
    button.pack()

    chances_label = tk.Label(root, text=f"Chances restantes: {len(word) + 2}")
    chances_label.pack()

    letterGuessed = ''
    chances = len(word) + 2
    correct = 0

    root.mainloop()