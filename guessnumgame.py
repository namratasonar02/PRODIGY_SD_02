import tkinter as tk
import random

class GuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guessing Game")
        self.window.configure(bg="#6495ED")  # blue background

        self.label = tk.Label(self.window, text="Guess a number between 1 and 100", bg="#6495ED", fg="#FFFFFF", font=("Arial", 24))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.window, width=20, font=("Arial", 24), bg="#CCCCCC", fg="#000000")
        self.entry.pack(pady=10)

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 18))
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="", bg="#6495ED", fg="#FFFFFF", font=("Arial", 18))
        self.result_label.pack(pady=10)

        self.attempts = 0
        self.number_to_guess = random.randint(1, 100)

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1
        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.", fg="#FF0000")  # red text
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.", fg="#FF0000")  # red text
        else:
            self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.", fg="#008000")  # green text
            self.button.config(state="disabled")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GuessingGame()
    game.run()
